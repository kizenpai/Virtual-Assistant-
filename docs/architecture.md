# NOVA System Architecture & Design Specification

This document provides a comprehensive technical breakdown of the architectural design, component interactions, concurrency patterns, and security principles implemented in **NOVA – AI-Powered Virtual Assistant**.

---

## 1. Architectural Overview

NOVA follows a **Layered Architecture** with an **Event-Driven Asynchronous Pipeline**. Responsibilities are partitioned into isolated modules to maintain high cohesion and low coupling.

```mermaid
flowchart TD
    subgraph UI ["Presentation Layer (CustomTkinter)"]
        GUI["NovaGUI Main Window"]
        Chat["Scrollable Conversation Frame"]
        MicBtn["Circular Mic Control"]
        Entry["Text Input Field"]
        Status["Dynamic Status Indicator"]
        Badge["AI Connection Pill"]
    end

    subgraph Core ["Coordination & Logic Layer"]
        Assistant["NovaAssistant (Central Coordinator)"]
        Router["CommandHandler (Smart Rule Engine)"]
        AIEngine["AIEngine (Google GenAI Client)"]
        STT["SpeechToText (SpeechRecognition)"]
        TTS["TextToSpeech (pyttsx3 Daemon Queue)"]
    end

    subgraph Utils ["Utility & Data Layer"]
        Calc["Safe Calculator (AST Evaluator)"]
        Notes["NotesManager (data/notes.txt)"]
        Logger["SensitiveDataFilter Logger"]
        Config["Configuration & .env Manager"]
    end

    GUI -->|User Input / Voice Click| Assistant
    Assistant -->|Check Built-in Rules| Router
    Router -->|Math Operations| Calc
    Router -->|Note Storage| Notes
    Router -->|Launch Apps / URLs| OS["Windows Subsystem / WebBrowser"]
    Assistant -->|Unmatched Queries| AIEngine
    AIEngine -->|Generative Query| Gemini["Google Gemini API Cloud"]
    Assistant -->|Audio Speech Output| TTS
    STT -->|Transcribed Text| Assistant
    Assistant -->|State Changes & Responses| GUI
```

---

## 2. Smart Command Routing Pipeline

When an input event (spoken or typed) is received, NOVA processes it through a strict tiered hierarchy to minimize API costs, avoid unnecessary latency, and maintain predictable system behavior:

```mermaid
flowchart TD
    Start(["Input: Voice or Text"]) --> Normalize["Normalize & Sanitize String"]
    Normalize --> ExitCheck{"Is Exit / Quit?"}
    ExitCheck -- Yes --> DoExit["Return Goodbye & Terminate Application"]
    ExitCheck -- No --> HelpCheck{"Is Help / Commands?"}
    HelpCheck -- Yes --> DoHelp["Return Formatted Command Reference"]
    HelpCheck -- No --> BuiltinCheck{"Matches Local Built-in Command?"}

    BuiltinCheck -- Yes --> ExecLocal["Execute Local Command:
    • DateTime
    • Application Launch (Notepad, Calc)
    • Website Open (YouTube, Google, GitHub)
    • Safe Math Calculator
    • Notes Management
    • Wikipedia Search
    • Joke Generator"]
    ExecLocal --> Output

    BuiltinCheck -- No --> KeyCheck{"Is Gemini API Key Configured?"}
    KeyCheck -- Yes --> CallGemini["Send Query to Gemini Chat Session
    (Multi-turn Session Context)"]
    CallGemini --> Output

    KeyCheck -- No --> Fallback["Return: 'AI mode is not configured.
    Please add your Gemini API key to the .env file.'"]
    Fallback --> Output

    Output["Deliver Output:
    1. Render Chat Bubble in GUI
    2. Enqueue in TTS Asynchronous Queue
    3. Update Status Indicator to Online"]
```

---

## 3. Asynchronous Concurrency Model

A major architectural challenge in desktop assistants is preventing blocking calls during audio capture, speech synthesis, and remote API calls. NOVA addresses this by running all time-intensive tasks on dedicated background threads:

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant GUI as CustomTkinter GUI (Main Thread)
    participant Worker as Background Worker Thread
    participant Assistant as NovaAssistant
    participant Engine as Gemini API / Command Router
    participant TTS as TTS Worker Thread (pyttsx3)

    User->>GUI: Click Microphone Button
    GUI->>GUI: Update Status: "Listening", Set Button to Active
    GUI->>Worker: Spawn Thread: listen_and_process()
    Worker->>Assistant: Capture Mic & Process
    Note over Worker: Audio capture & Google STT (3-5s)
    Worker->>Engine: Route input (Built-in or Gemini)
    Engine-->>Worker: Return Response String
    Worker->>GUI: root.after(0, update_chat_and_status)
    GUI->>GUI: Render User & NOVA Message Bubbles
    Worker->>TTS: tts.speak(response_text)
    Note over TTS: Background Audio Synthesis
    TTS->>GUI: root.after(0, set_status("Speaking"))
    TTS->>TTS: Play speech through sound device
    TTS->>GUI: root.after(0, set_status("Online"))
```

---

## 4. Class & Component Structure

```mermaid
classDiagram
    class NovaAssistant {
        +CommandHandler command_handler
        +AIEngine ai_engine
        +SpeechToText stt
        +TextToSpeech tts
        +process_input(user_text: str) dict
        +listen_and_process() dict
        +set_speech_enabled(enabled: bool)
        +reload_ai_config() bool
        +shutdown()
    }

    class CommandHandler {
        +normalize(text: str) str
        +handle(raw_input: str) dict
        -_handle_greetings(text: str)
        -_handle_datetime(text: str)
        -_handle_apps(text: str)
        -_handle_websites(text: str)
        -_handle_calculator(text: str)
        -_handle_notes(text: str)
    }

    class AIEngine {
        +str api_key
        +str model_name
        +genai.Client client
        +chats.Chat chat_session
        +is_configured() bool
        +generate_response(prompt: str) str
        +reset_chat()
        +reload_config() bool
    }

    class TextToSpeech {
        +Queue queue
        +bool is_enabled
        +speak(text: str)
        +stop()
        +set_enabled(bool)
        +shutdown()
    }

    class SpeechToText {
        +Recognizer recognizer
        +bool is_available()
        +listen_once(timeout, phrase_limit) tuple
    }

    class NovaGUI {
        +NovaAssistant assistant
        +_build_header()
        +_build_status_bar()
        +_build_chat_area()
        +_build_input_controls()
        +_on_mic_clicked()
        +_on_send_clicked()
        +_add_message_bubble(sender, text, is_user)
    }

    NovaGUI --> NovaAssistant
    NovaAssistant --> CommandHandler
    NovaAssistant --> AIEngine
    NovaAssistant --> SpeechToText
    NovaAssistant --> TextToSpeech
```

---

## 5. Security Architecture

1. **Zero Unsafe `eval()` / `exec()` Execution:**
   - Mathematical expressions are parsed strictly into Abstract Syntax Trees using Python's `ast.parse(expr, mode='eval')`.
   - Only approved nodes (`ast.Constant`, `ast.BinOp`, `ast.UnaryOp`, `ast.Call`) and safe functions (`sqrt`, `sin`, `log`, etc.) are evaluated.
   - Code injection attempts like `__import__('os').system(...)` are rejected at the AST root.

2. **Strict Application Whitelisting:**
   - Operating system application launching is restricted to approved system tools: `notepad.exe` and `calc.exe`.
   - General shell execution of arbitrary commands from spoken text is strictly blocked.

3. **API Key Isolation & Redaction:**
   - API keys are never stored in source code; they are loaded via `.env` files.
   - `.env` is excluded in `.gitignore` to prevent accidental version control commits.
   - `utils.logger.SensitiveDataFilter` runs a regex pass on all log messages, masking any detected API key patterns before writing to `logs/nova.log`.

---

## 6. Directory Layout & Module Responsibilities

```
NOVA/
├── main.py                  # CLI / GUI entry point
├── config.py                # Environment and styling configuration
├── requirements.txt         # Core dependencies
├── launch.bat               # Windows one-click launcher
├── .env.example             # Configuration template
├── .gitignore               # Version control exclusion rules
│
├── core/
│   ├── assistant.py         # Central coordinator
│   ├── command_handler.py   # Deterministic command router
│   ├── ai_engine.py         # Google Gemini integration
│   ├── speech_to_text.py    # Microphone audio capture
│   └── text_to_speech.py    # Asynchronous voice synthesizer
│
├── gui/
│   └── interface.py         # CustomTkinter dashboard
│
├── utils/
│   ├── calculator.py        # Safe AST arithmetic evaluator
│   ├── notes_manager.py     # Local notes storage
│   └── logger.py            # Sanitized rotating logger
│
├── data/
│   └── notes.txt            # Persistent user notes
│
├── docs/
│   ├── project_report.md    # College academic report
│   ├── architecture.md      # System design and specifications
│   └── viva_questions.md    # Academic viva voce Q&A
│
└── tests/
    ├── test_commands.py     # Command routing test suite
    ├── test_calculator.py   # Arithmetic test suite
    ├── test_notes.py        # Notes management test suite
    └── test_ai_engine.py    # AI engine test suite
```

