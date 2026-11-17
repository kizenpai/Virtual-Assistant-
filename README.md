# EDITH – AI-Powered Desktop Virtual Assistant

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![GUI-CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-00D2FF.svg)](https://github.com/TomSchimansky/CustomTkinter)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini%20(google--genai)-4285F4.svg)](https://aistudio.google.com/)
[![Design: Kombai Prism](https://img.shields.io/badge/Design-Kombai%20Prism%20Minimalism-F7F6F2.svg)](https://kombai.com/gallery/inspirations/prism/)
[![Tests](https://img.shields.io/badge/Tests-35%20Passed-10B981.svg)](tests/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**EDITH (Even Dead, I'm The Hero)** is an intelligent, multi-modal desktop assistant built in Python for an **Artificial Intelligence Laboratory** project. EDITH combines speech recognition, text-to-speech synthesis, local computer automation, and Google Gemini artificial intelligence into an exhibition-grade minimalist interface inspired by **Kombai's "Prism"** design system.

---

## 🌟 Key Features

- **🏛️ Kombai "Prism" Exhibition UI:** Pure black canvas (`#050505`), soft ivory typography, hairline architectural dividers, and an iridescent chromatic glass ring artifact.
- **✨ Two-Stage Experience:**
  - **Stage 1 (Exhibition Landing):** Pinned-corner metadata, centered 3D iridescent ring, majestic Georgia Serif wordmark (`E D I T H`), manifesto line, and progressive neural synchronization bar.
  - **Stage 2 (Working Workspace):** Automatic smooth transition into a focused productivity space with conversational history, system prompts, and floating interaction dock.
- **🎙️ Voice Recognition:** Speak naturally through your microphone; EDITH transcribes speech into text using Google Speech Recognition with automated ambient noise calibration.
- **🔊 Asynchronous Text-to-Speech:** Real-time voice responses via `pyttsx3` running on a background worker thread (GUI never freezes).
- **🤖 Google Gemini AI Integration:** Seamlessly handles complex, open-ended conversational questions using Google's official `google-genai` SDK.
- **🛡️ Graceful Offline Degradation:** Works out-of-the-box in basic offline mode **without an API key**; built-in commands remain fully operational.
- **⚡ Smart Command Routing:** Prioritizes local deterministic tasks (zero latency, zero API cost) and escalates only unmatched queries to Gemini.
- **🧮 Safe Math Calculator:** Evaluates mathematical expressions using Python's Abstract Syntax Tree (`ast`) without unsafe `eval()`.
- **📝 Personal Notes Manager:** Quickly save, list, and clear persistent timestamped notes stored in `data/notes.txt`.
- **💻 Safe Desktop Automation:** Open Notepad, Calculator, the web browser, Google Search, Wikipedia, and specific websites safely.
- **🧪 100% Automated Test Coverage:** Comprehensive test suite with 35 `pytest` unit tests verifying all core subsystems.

---

## 🏗️ Project Architecture

```
EDITH/
├── main.py                  # Application entry point (GUI & CLI modes)
├── config.py                # Central configuration & .env management
├── requirements.txt         # Project package dependencies
├── launch.bat               # Windows double-click launcher
├── .env                     # Local environment file (contains your API key)
├── .env.example             # Environment template
├── .gitignore               # Version control exclusion rules
│
├── core/
│   ├── assistant.py         # Main assistant coordinator & routing pipeline
│   ├── command_handler.py   # Deterministic command router & automation
│   ├── ai_engine.py         # Google Gemini integration via google-genai
│   ├── speech_to_text.py    # Microphone audio capture & STT
│   └── text_to_speech.py    # Asynchronous non-blocking voice synthesis
│
├── gui/
│   └── interface.py         # CustomTkinter Kombai Prism Gallery UI
│
├── utils/
│   ├── calculator.py        # Safe AST mathematical expression evaluator
│   ├── notes_manager.py     # Local notes persistence manager
│   └── logger.py            # Sanitized rotating file & console logger
│
├── data/
│   └── notes.txt            # Stored user notes
│
├── assets/
│   ├── prism_ring.png       # 3D iridescent chromatic glass ring artifact
│   └── prism_ring_small.png # Scaled chromatic ring icon
│
├── docs/
│   ├── project_report.md    # Full 19-section college project report
│   ├── architecture.md      # Architectural diagrams & design specifications
│   └── viva_questions.md    # 25+ detailed viva voce questions & answers
│
└── tests/
    ├── test_commands.py     # Command parsing & routing tests
    ├── test_calculator.py   # Arithmetic & security tests
    ├── test_notes.py        # Notes management tests
    └── test_ai_engine.py    # Gemini configuration & fallback tests
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- **Operating System:** Windows 10 or Windows 11 (64-bit).
- **Python:** Python 3.10, 3.11, 3.12, or 3.13.
- **Microphone & Speakers:** Working audio input/output devices.

### 2. Installation
Open PowerShell or Command Prompt in the project directory:

```powershell
# Optional: Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Google Gemini API Key Setup

> [!NOTE]
> `.env` has been unignored from `.gitignore` so your configured key is tracked. If you publish to a **public** GitHub repository, GitHub Secret Scanning or Google may automatically detect and revoke public keys. For public repositories, recommend keeping `.env` private and using `.env.example`.

Your `.env` file is located at the project root:

```ini
# EDITH Environment Configuration
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
GEMINI_MODEL=gemini-2.5-flash
```

When you launch EDITH, the badge in the top right will display **`GEMINI // GEMINI-2.5-FLASH`** and all general questions will be answered by Gemini!

---

## 🖥️ How to Launch EDITH

### Option A: One-Click Launcher (Windows)
Double-click `launch.bat` in the project root. It will automatically detect Python and start EDITH.

### Option B: Terminal Command (GUI Mode)
```powershell
python main.py
```

### Option C: Terminal CLI Mode (Headless / Fast Testing)
```powershell
python main.py --cli
```

---

## 🗣️ Supported Voice & Text Commands

You can speak to EDITH using the 🎤 Microphone button or type commands directly into the text field:

| Category | Example Phrases | EDITH Action |
| :--- | :--- | :--- |
| **Greetings** | `"Hello"`, `"Hi EDITH"`, `"Good morning"` | Responds with a polite, time-appropriate greeting |
| **Identity** | `"Who are you?"`, `"What is your purpose?"` | Introduces EDITH and its cognitive capabilities |
| **Date & Time** | `"What time is it?"`, `"What is today's date?"` | Reports current local time or date |
| **Applications** | `"Open Notepad"`, `"Open Calculator"`, `"Open Browser"` | Safely launches desktop applications |
| **Websites** | `"Open YouTube"`, `"Open Google"`, `"Open GitHub"`, `"Open Gmail"` | Opens the requested service in your browser |
| **Custom URL** | `"Open website reddit.com"` | Opens the target website |
| **Web Search** | `"Search Google for quantum computing"` | Executes a Google search query in browser |
| **Wikipedia** | `"Wikipedia Alan Turing"`, `"Search Wikipedia for Mars"` | Summarizes factual information in 2 sentences |
| **Math Calculator**| `"Calculate 25 * 4"`, `"What is 100 divided by 5"`, `"5 + 5"` | Safely evaluates expression without `eval()` |
| **Notes - Save** | `"Save note remember to submit AI lab project"`, `"Note call mentor"` | Appends timestamped note to `data/notes.txt` |
| **Notes - Read** | `"Read notes"`, `"Show my notes"`, `"List notes"` | Displays all saved personal notes |
| **Notes - Clear**| `"Clear notes"` | Clears all stored notes |
| **Jokes** | `"Tell me a joke"`, `"Make me laugh"` | Shares a random programming or science joke |
| **Help** | `"Help"`, `"What can you do?"`, `"Commands"` | Shows complete command reference |
| **AI Questions** | *"Explain how neural networks learn"*, *"Write Python code for binary search"* | Routes to Google Gemini for concise, intelligent response |
| **Exit** | `"Exit"`, `"Quit"`, `"Close EDITH"`, `"Goodbye"` | Speaks farewell and closes application |

---

## 🧪 Running Automated Tests

EDITH includes an automated test suite powered by `pytest`. Run all tests using:

```powershell
python -m pytest tests/ -v
```

**Test Results:**
```
tests/test_ai_engine.py::test_ai_engine_unconfigured_default PASSED      [  2%]
tests/test_ai_engine.py::test_ai_engine_placeholder_key PASSED           [  5%]
tests/test_ai_engine.py::test_ai_engine_status_info PASSED               [  8%]
tests/test_ai_engine.py::test_ai_engine_configured_mocked PASSED         [ 11%]
tests/test_calculator.py::test_basic_addition PASSED                     [ 17%]
tests/test_calculator.py::test_division_by_zero PASSED                   [ 37%]
tests/test_calculator.py::test_disallowed_code_injection PASSED          [ 45%]
tests/test_commands.py::test_greeting_commands PASSED                    [ 48%]
tests/test_commands.py::test_open_youtube PASSED                         [ 62%]
tests/test_commands.py::test_open_notepad PASSED                         [ 80%]
tests/test_commands.py::test_unmatched_routes_to_ai PASSED               [ 85%]
tests/test_notes.py::test_save_and_read_note PASSED                      [ 88%]
tests/test_notes.py::test_clear_notes PASSED                             [100%]
======================== 35 passed in 1.57s ========================
```

---

## 🛠️ Troubleshooting

### 1. Microphone Not Detected or Speech Recognition Fails
- Ensure your microphone is plugged in and set as the **Default Input Device** in Windows Settings -> System -> Sound.
- Check that microphone access is enabled under **Windows Settings -> Privacy & Security -> Microphone**.
- **Alternative:** You can always interact with EDITH by typing in the input box; the text box is 100% functional even without a microphone.

### 2. PyAudio Installation on Windows
If `pip install pyaudio` fails, install the precompiled wheel using:
```powershell
pip install pipwin
pipwin install pyaudio
```

### 3. Voice Output (TTS) is Silent
- Verify that your speakers/headphones are unmuted.
- Ensure the **VOICE** switch in the top-right corner of the EDITH window is turned **ON**.

### 4. Gemini AI Returns "AI mode is not configured"
- Open `.env` and verify that `GEMINI_API_KEY` has your actual key without quotes or spaces:
  ```ini
  GEMINI_API_KEY=YOUR_KEY_HERE
  ```
- Restart the application.

---

## 📚 Academic Documentation

- 📄 **Project Report:** See [`docs/project_report.md`](docs/project_report.md) for a comprehensive 19-section academic report.
- 📐 **Architecture Documentation:** See [`docs/architecture.md`](docs/architecture.md) for detailed Mermaid diagrams and system data flows.
- 🎓 **Viva Questions & Answers:** See [`docs/viva_questions.md`](docs/viva_questions.md) for 25+ academic viva voce preparation questions.

---

## 📄 License
Developed for academic purposes under the MIT License.
