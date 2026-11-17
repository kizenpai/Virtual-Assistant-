# PROJECT REPORT: NOVA – AI-POWERED VIRTUAL ASSISTANT

**Academic Project Report submitted in partial fulfillment of the requirements for the Degree of Bachelor of Technology (B.Tech) in Computer Science and Engineering / Artificial Intelligence**

---

## 1. Title Page Information

- **Project Title:** NOVA – AI-Powered Virtual Assistant
- **Course / Lab:** Artificial Intelligence Laboratory (AI Lab)
- **Degree:** Bachelor of Technology (B.Tech)
- **Discipline:** Computer Science and Engineering / Artificial Intelligence
- **Platform:** Windows 11 Desktop Application
- **Language & Frameworks:** Python 3.11+, CustomTkinter, Google Gemini SDK (`google-genai`), SpeechRecognition, pyttsx3
- **Academic Year:** 2026–2027

---

## 2. Abstract

In modern computing, human-computer interaction (HCI) has evolved rapidly from text-based command interfaces to intelligent voice-driven virtual assistants. **NOVA (Neural Omnipresent Virtual Assistant)** is an intelligent, multi-modal desktop assistant built in Python. NOVA integrates speech-to-text recognition, text-to-speech synthesis, rule-based natural language command processing, and large language model (LLM) reasoning via the official Google Gemini SDK (`google-genai`).

The architecture follows a dual-mode smart routing pipeline: routine desktop commands (such as application launching, website navigation, time/date queries, Wikipedia lookups, mathematical calculations, and personal notes management) are processed locally with near-zero latency and deterministic precision. Conversely, open-ended conceptual queries, coding questions, and general inquiries are routed to Google's Gemini generative AI model while preserving multi-turn conversational context. Crucially, the system features a graceful degradation mechanism: NOVA operates seamlessly in an offline/built-in mode without an API key, providing helpful notifications and automatically enabling advanced AI capabilities upon key configuration. The user interface is developed with CustomTkinter, delivering a responsive, dark futuristic aesthetic designed for optimal usability and thread safety.

---

## 3. Introduction

Virtual assistants such as Apple Siri, Amazon Alexa, and Google Assistant have demonstrated the transformative potential of conversational interfaces. However, proprietary commercial assistants often suffer from high opacity, lack of customization, and cloud dependency for even trivial local operations.

NOVA is engineered as an open, modular, extensible virtual assistant specifically designed for educational demonstration and practical utility. It bridges local deterministic automation with state-of-the-art cloud-based generative AI. By leveraging asynchronous multithreading, NOVA decouples audio processing, speech synthesis, and network API communications from the graphical user interface (GUI), ensuring smooth visual feedback and eliminating application freezes.

---

## 4. Problem Statement

Existing desktop automation and voice interaction systems suffer from several distinct shortcomings:

1. **Tight Coupling to Cloud Services:** Many assistants fail to perform basic offline tasks (such as taking notes, solving arithmetic, or opening applications) when Internet or API connectivity is severed.
2. **Brittle Interface Responsiveness:** Audio listening and remote API calls in naive Python desktop apps frequently block the main event loop, causing GUI unresponsiveness or application crashes.
3. **Rigid Command Matching:** Simple regex or keyword assistants fail when faced with open-domain questions or variations in speech phrasing.
4. **Lack of Safe Execution:** Arbitrary shell execution from natural language inputs creates severe security vulnerabilities on user endpoints.

NOVA addresses these challenges through a modular architecture, thread-safe asynchronous queues, AST-based safe evaluation, restricted application launching, and intelligent fallback to Google Gemini AI.

---

## 5. Objectives

The primary objectives of the NOVA project include:

1. **Multi-Modal Interaction:** Enable bidirectional interaction through microphone speech input, text-to-speech audio output, and intuitive GUI text entry.
2. **Smart Hybrid Routing:** Implement an intelligent decision pipeline that prioritizes local deterministic actions before falling back to remote LLM processing.
3. **Robust Fault Tolerance:** Ensure the assistant runs out of the box in offline mode without requiring a Gemini API key during initial startup or basic tasks.
4. **Desktop Automation & Utility:** Provide safe, sandboxed desktop tools including an AST mathematical calculator, timestamped notes manager, browser launcher, and application starter.
5. **Modern AI Dashboard:** Construct an aesthetically engaging, dark-mode futuristic dashboard using CustomTkinter that visually tracks assistant states (Online, Listening, Processing, Speaking, Offline).
6. **Thread Safety & Responsiveness:** Isolate audio I/O and network operations in background worker threads.

---

## 6. Scope of the Project

### In-Scope
- Voice speech recognition via Google Web Speech API through the `SpeechRecognition` library.
- Natural offline Text-to-Speech synthesis using `pyttsx3`.
- Conversational artificial intelligence via the official `google-genai` Python SDK.
- Safe arithmetic parser supporting mathematical functions, powers, and natural language arithmetic.
- Persistent local notes storage (`data/notes.txt`).
- Safe execution of approved Windows applications (Notepad, Calculator, Web Browser).
- Automated test suite validating core subsystems via `pytest`.

### Out-of-Scope
- Direct system hardware control (e.g. BIOS modifications, kernel drivers).
- Automatic execution of destructive administrative commands (e.g., formatting disks, deleting system trees).
- Local hosting of multi-billion parameter LLMs (relies on cloud-based API to minimize local hardware requirements).

---

## 7. Hardware Requirements

- **Processor:** Intel Core i3 / AMD Ryzen 3 or higher (tested on Intel Core i5 / AMD Ryzen 5+).
- **RAM:** Minimum 4 GB RAM (8 GB or 16 GB recommended).
- **Audio Input:** USB microphone, 3.5mm headset, or integrated laptop microphone.
- **Audio Output:** Integrated speakers or headphones.
- **Graphics:** Standard integrated display adapter or dedicated GPU (runs entirely on CPU without requiring GPU acceleration).
- **Storage:** 500 MB free hard disk space.

---

## 8. Software Requirements

- **Operating System:** Windows 10 / Windows 11 (64-bit).
- **Programming Language:** Python 3.10, 3.11, 3.12, or 3.13.
- **Shell / Command Environment:** Windows PowerShell or Command Prompt.
- **Network:** Active internet connection for Gemini API queries, SpeechRecognition Google backend, and Wikipedia lookups.

---

## 9. Technologies Used

| Technology / Library | Version | Purpose in Project |
| :--- | :--- | :--- |
| **Python** | 3.11 / 3.13 | Core programming language |
| **CustomTkinter** | >= 5.2.0 | Modern dark-themed graphical dashboard |
| **google-genai** | >= 0.1.1 | Official Google Gemini Python SDK for generative intelligence |
| **SpeechRecognition** | >= 3.10.0 | Captures and translates acoustic speech to text |
| **PyAudio** | >= 0.2.14 | PortAudio bindings for microphone stream acquisition |
| **pyttsx3** | >= 2.90 | Offline text-to-speech voice synthesis engine |
| **python-dotenv** | >= 1.0.0 | Secure loading of environment variables from `.env` |
| **wikipedia** | >= 1.4.0 | Factual summary retrieval from Wikipedia API |
| **requests** | >= 2.31.0 | Standard HTTP client for network operations |
| **pytest** | >= 7.0.0 | Automated unit and integration testing framework |

---

## 10. System Architecture

NOVA is architected using a layered, modular software pattern:

```
+------------------------------------------------------------------+
|                    PRESENTATION LAYER (GUI)                      |
|       CustomTkinter Dashboard (Chat View, Mic, Entry, Status)    |
+------------------------------------------------------------------+
                                 │
                                 ▼
+------------------------------------------------------------------+
|                    COORDINATION LAYER (Assistant)                |
|        NovaAssistant (Smart Routing Pipeline, Event Dispatch)    |
+------------------------------------------------------------------+
         │                         │                        │
         ▼                         ▼                        ▼
+--------------------+   +-------------------+   +--------------------+
|  INPUT SUBSYSTEM   |   |   CORE ROUTING    |   |  OUTPUT SUBSYSTEM  |
|  SpeechRecognition |   |  CommandHandler   |   |  pyttsx3 (TTS)     |
|  (STT Engine)      |   |  (Rule Engine)    |   |  (Worker Queue)    |
+--------------------+   +-------------------+   +--------------------+
                                   │
         ┌─────────────────────────┴────────────────────────┐
         ▼                                                  ▼
+--------------------+                             +------------------+
|   LOCAL TOOLS      |                             |   AI ENGINE      |
| • Safe Calculator  |                             | • google-genai   |
| • Notes Manager    |                             | • Gemini Model   |
| • System Launcher  |                             | • Multi-turn Chat|
+--------------------+                             +------------------+
```

---

## 11. Module Descriptions

### 1. `main.py`
The application's entry point. Parses command line arguments, handles runtime exceptions, and directs launch into either GUI mode (`run_gui_mode()`) or terminal headless mode (`run_cli_mode()`).

### 2. `config.py`
Centralized repository for operational configuration. Manages absolute filesystem paths, resolves `.env` variables, stores UI color themes, and sets speech parameters.

### 3. `core/assistant.py`
The central orchestrator. Implements `process_input()` and `listen_and_process()`. Coordinates communication between the command router, TTS worker, speech recognizer, and Gemini AI engine.

### 4. `core/command_handler.py`
The deterministic rule engine. Uses regular expressions to parse greetings, dates, times, jokes, application launches, notes requests, and web URLs. Flags unmatched queries as `is_ai_candidate`.

### 5. `core/ai_engine.py`
The generative AI bridge using Google's official `google-genai` SDK. Instantiates `genai.Client`, manages multi-turn `chats.create()` sessions with system instructions, and implements error handling for invalid keys, rate limits, and network dropouts.

### 6. `core/speech_to_text.py`
Audio acquisition module. Configures ambient noise calibration, microphone device verification, and Google speech recognition with timeout handling.

### 7. `core/text_to_speech.py`
Non-blocking voice synthesizer using `pyttsx3`. Utilizes a `queue.Queue` with a background daemon thread to process speech sequentially without blocking the GUI.

### 8. `gui/interface.py`
CustomTkinter dashboard. Features styled chat message cards, visual glowing logo, dynamic status indicator, circular microphone trigger, quick action toolbar, and thread-safe UI updates.

### 9. `utils/calculator.py`
Safe mathematical evaluator. Converts natural language queries into expressions and parses AST nodes without unsafe `eval()`. Supports arithmetic operators, powers, and standard trigonometric/logarithmic functions.

### 10. `utils/notes_manager.py`
Persistent notes manager. Provides timestamped append operations, formatted retrieval, and clearing for `data/notes.txt`.

### 11. `utils/logger.py`
Thread-safe rotating file and stream logger with an integrated regex sanitizer to prevent API keys from leaking into log files.

---

## 12. Working Methodology

1. **User Interaction:** The user speaks into the microphone by clicking the circular mic button or types text into the input field and presses Send / Enter.
2. **Input Ingestion:**
   - Voice input is captured by `SpeechToText.listen_once()`, adjusted for ambient room noise, and transcribed into text.
   - Text input is captured directly from the entry widget.
3. **Normalization:** Input is sanitized by stripping leading/trailing whitespace, punctuation, and converting to lowercase.
4. **Smart Command Evaluation:**
   - `CommandHandler.handle()` searches for matching built-in patterns.
   - If matched, the command executes locally (e.g. opens browser, evaluates math, saves note) and returns a formatted response.
5. **AI Routing:**
   - If no built-in pattern matches, the query is marked as an AI candidate.
   - If `GEMINI_API_KEY` is present, the prompt is dispatched to Gemini.
   - If `GEMINI_API_KEY` is absent, the assistant returns: `"AI mode is not configured. Please add your Gemini API key to the .env file."`
6. **Output Delivery:**
   - The response bubble is rendered in the GUI chat window.
   - Asynchronous TTS enqueues the sanitized response text and speaks it through the sound card.
   - Status indicators update in real time.

---

## 13. Algorithms and Workflow

### Smart Routing Algorithm
```
Input: Raw string S from Voice or Text
Output: Response text R, Action A, Status flag F

1. Normalize S -> S_norm
2. If S_norm matches EXIT_PATTERN:
     Set R = "Goodbye!", A = EXIT, Return
3. If S_norm matches HELP_PATTERN:
     Set R = HELP_TEXT, A = SHOW_HELP, Return
4. If S_norm matches GREETING / DATETIME / JOKE:
     Compute local deterministic response -> R, Return
5. If S_norm matches NOTE_PATTERN:
     Call notes_manager -> R, Return
6. If S_norm matches APP_LAUNCH_PATTERN:
     Execute approved process -> R, Return
7. If S_norm matches MATH_PATTERN:
     Call SafeEvaluator(AST(S_norm)) -> R, Return
8. If S_norm matches SEARCH_PATTERN / WIKIPEDIA:
     Call browser or wikipedia API -> R, Return
9. Unmatched Query (General Question):
     If GEMINI_API_KEY is configured:
         Try:
             Send to Gemini Chat Session -> R
         Catch Exception E:
             Map E to friendly diagnostic message -> R
     Else:
         Set R = "AI mode is not configured. Please add your Gemini API key to the .env file."
10. Return R
```

### Safe Mathematical AST Evaluation Algorithm
```
Input: AST Node N
Output: Numeric result (int or float)

1. If N is Constant/Num: Return N.value
2. If N is UnaryOp(+ or -): Return Op(Evaluate(N.operand))
3. If N is BinOp:
     L = Evaluate(N.left)
     R = Evaluate(N.right)
     If Op is Division and R == 0: Throw ZeroDivisionError
     If Op is Power and (abs(L) > 10000 or abs(R) > 1000): Throw OverflowError
     Return Op(L, R)
4. If N is Call:
     Validate function name in SAFE_FUNCTIONS
     Evaluate arguments
     Return Function(*args)
5. Else: Throw ValueError("Unsupported syntax")
```

---

## 14. Implementation Details

- **Language Standard:** Python 3.11 / 3.13 compatible.
- **Asynchronous Decoupling:** Uses Python's standard `threading.Thread(daemon=True)` for worker tasks. Communication between the worker thread and CustomTkinter is mediated via `widget.after(0, callback)` to ensure GUI thread safety.
- **Input Sanitization for TTS:** Markdown markers (such as bold stars, backticks, URLs, code blocks) are stripped using regular expressions before dispatching strings to the speech engine, producing natural pronunciation.
- **AST Safety:** Completely eliminates `eval()` and `exec()`, preventing remote code execution (RCE) via text input.

---

## 15. Testing

The project was validated using an automated test suite developed with `pytest`. Mocking was utilized via `unittest.mock` to isolate external dependencies (such as sound hardware, live browsers, and remote APIs).

### Test Matrix

| Test Suite | File | Tests Run | Result |
| :--- | :--- | :--- | :--- |
| **Command Processing** | `tests/test_commands.py` | 14 | 14 Passed |
| **Calculator Operations** | `tests/test_calculator.py` | 12 | 12 Passed |
| **Notes Management** | `tests/test_notes.py` | 5 | 5 Passed |
| **Gemini AI Engine** | `tests/test_ai_engine.py` | 4 | 4 Passed |
| **Total Automated Tests** | | **35** | **35 Passed (100%)** |

### Verified Scenarios:
1. Greetings, time, and date command matching across various phrasing variants.
2. Web navigation to Google, YouTube, GitHub, and custom domains.
3. Safe application launching (Notepad, Calculator).
4. Wikipedia summarization handling.
5. Arithmetic operations: addition, subtraction, multiplication, division, modulo, exponentiation, and domain functions.
6. Division by zero, malformed syntax, and code injection prevention.
7. Notes file persistence, formatting, and clearing.
8. Unconfigured API key fallback message: `"AI mode is not configured. Please add your Gemini API key to the .env file."`
9. Mocked Gemini conversational response generation.

---

## 16. Limitations

1. **Internet Dependency for Speech-to-Text:** The default `SpeechRecognition` Google Web Speech recognizer requires active internet connectivity.
2. **Microphone Device Dependency:** Systems lacking an audio input device fall back to text input (though fully supported in the GUI).
3. **Restricted Local Automation:** Computer automation is intentionally constrained to pre-approved executables to prevent arbitrary command execution.
4. **Third-Party API Rate Limits:** Free-tier Gemini API keys are subject to Google AI Studio RPM (requests per minute) quotas.

---

## 17. Future Enhancements

1. **Offline Automatic Speech Recognition:** Integration of offline models (e.g., Whisper-small or Vosk) to enable completely offline voice recognition.
2. **Custom Wake Word Detection:** Adding local wake-word models (e.g., OpenWakeWord or Porcupine) to trigger listening on "Hey NOVA".
3. **System IoT & Smart Home Integration:** Integrating Home Assistant or MQTT protocols for controlling lights, thermostats, and IoT devices.
4. **Desktop Screen Understanding:** Implementing multi-modal vision models (Gemini Flash Vision) to allow NOVA to inspect and answer questions about on-screen content.

---

## 18. Conclusion

The **NOVA Virtual Assistant** project successfully accomplishes all specified objectives. It delivers an intuitive, multi-modal desktop assistant combining voice and text input, speech synthesis, local computer automation, and Google Gemini artificial intelligence.

By following sound software engineering principles—including modular separation of concerns, asynchronous thread safety, safe AST parsing, and robust exception handling—NOVA functions reliably across varying network states and hardware configurations. It serves as an exemplary academic and practical demonstration of modern AI and Human-Computer Interaction principles in Python.

---

## 19. References

1. Google DeepMind. *Google Gen AI Python SDK Documentation*. https://googleapis.github.io/python-genai/
2. CustomTkinter Documentation. *Modern UI Library for Python*. https://customtkinter.tomschimansky.com/
3. SpeechRecognition Documentation. *Library for performing speech recognition*. https://pypi.org/project/SpeechRecognition/
4. Microsoft Speech API (SAPI5) and pyttsx3. *Text to Speech (TTS) library for Python 2 and 3*. https://pyttsx3.readthedocs.io/
5. Python Software Foundation. *Python 3 Standard Library: `ast`, `threading`, `queue`, `subprocess`*. https://docs.python.org/3/
6. Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach (4th ed.)*. Pearson.

