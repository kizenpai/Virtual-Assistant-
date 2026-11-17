"""
Configuration Module for NOVA - AI-Powered Virtual Assistant.

Handles environment variables, application paths, UI styling constants,
and operational parameters for speech, logging, and AI models.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# Windows System PATH Sanitization (Prevents MSYS2 DLL Relocation Conflicts)
# -----------------------------------------------------------------------------
if sys.platform == "win32":
    current_path = os.environ.get("PATH", "").split(";")
    filtered_path = [p for p in current_path if "msys64" not in p.lower() and "cygwin" not in p.lower()]
    preferred = [
        r"D:\anaconda3",
        r"D:\anaconda3\Scripts",
        r"D:\anaconda3\Library\bin",
        r"C:\Windows\system32",
        r"C:\Windows"
    ]
    os.environ["PATH"] = ";".join(preferred + [p for p in filtered_path if p not in preferred])

# -----------------------------------------------------------------------------
# Base Directories & Paths
# -----------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"
ASSETS_DIR = BASE_DIR / "assets"
DOCS_DIR = BASE_DIR / "docs"
NOTES_FILE = DATA_DIR / "notes.txt"

# Ensure runtime directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# Environment & API Key Configuration
# -----------------------------------------------------------------------------
# Load environment variables from .env file located at workspace root
ENV_FILE = BASE_DIR / ".env"
if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE, override=True)
else:
    load_dotenv(override=True)

# Google Gemini API Settings
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

def is_gemini_configured() -> bool:
    """Check whether a valid non-empty Gemini API key is configured."""
    key = os.getenv("GEMINI_API_KEY", "").strip()
    return bool(key and key != "YOUR_GEMINI_API_KEY_HERE" and len(key) > 10)

def get_gemini_api_key() -> str:
    """Retrieve the current Gemini API key."""
    return os.getenv("GEMINI_API_KEY", "").strip()

def get_gemini_model() -> str:
    """Retrieve the configured Gemini model identifier."""
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

# -----------------------------------------------------------------------------
# Application Metadata
# -----------------------------------------------------------------------------
APP_NAME = "EDITH"
APP_TITLE = "EDITH – AI Virtual Assistant"
APP_SUBTITLE = "Even Dead, I'm The Hero | Your Personal AI Companion"
APP_VERSION = "1.0.0"
APP_AUTHOR = "B.Tech AI Lab Project"

# -----------------------------------------------------------------------------
# Speech Recognition & Synthesis Parameters
# -----------------------------------------------------------------------------
# Text-to-Speech (pyttsx3)
TTS_RATE = 175             # Words per minute
TTS_VOLUME = 1.0           # Range 0.0 to 1.0
TTS_ENABLED_DEFAULT = True # Voice output enabled by default

# Speech-to-Text (SpeechRecognition)
STT_ENERGY_THRESHOLD = 250 # Microphone sensitivity (lower is more sensitive)
STT_LISTEN_TIMEOUT = 10    # Generous seconds to wait for speech to begin
STT_PHRASE_TIME_LIMIT = 15 # Maximum seconds per speech phrase

# -----------------------------------------------------------------------------
# UI Theme & Color Palette (Kombai "Prism" Gallery Minimalism Aesthetic)
# -----------------------------------------------------------------------------
# Pure black canvas with soft ivory type and iridescent chromatic glass ring
COLOR_BG_PRIMARY = "#050505"      # Pure Black Gallery Canvas
COLOR_BG_SECONDARY = "#0C0C0C"    # Obsidian Panel surface
COLOR_BG_TERTIARY = "#141414"     # Card Surface / Chat Card
COLOR_BG_INPUT = "#0D0D0D"        # Minimalist Entry Field

COLOR_BORDER_HAIRLINE = "#1E1E1E" # 1px Architectural Hairline
COLOR_BORDER_LIGHT = "#2A2A2A"    # Focused Hairline

COLOR_ACCENT_CYAN = "#00F5D4"     # Iridescent Cyan highlight
COLOR_ACCENT_BLUE = "#4CC9F0"     # Chromatic Sky Blue
COLOR_ACCENT_VIOLET = "#7B2CBF"   # Iridescent Violet
COLOR_ACCENT_MAGENTA = "#F72585"  # Chromatic Magenta
COLOR_ACCENT_HOVER = "#1A1A1A"    # Subdued Gallery Hover
COLOR_ACCENT_BORDER = "#1E1E1E"   # Hairline Border

# Typography Palette: Soft Ivory & Exhibition Warm Grays
COLOR_TEXT_PRIMARY = "#F7F6F2"    # Soft Ivory
COLOR_TEXT_SECONDARY = "#9E9D98"  # Exhibition Warm Gray
COLOR_TEXT_MUTED = "#5A5954"      # Muted Metadata Gray

# Status Indicator Colors
STATUS_ONLINE = "#10B981"         # Subtle Emerald
STATUS_LISTENING = "#F59E0B"      # Warm Amber
STATUS_PROCESSING = "#A855F7"     # Chromatic Violet
STATUS_SPEAKING = "#00F5D4"       # Iridescent Cyan
STATUS_OFFLINE = "#EF4444"        # Crimson

# Chat Bubble Colors
BUBBLE_USER = "#121212"           # Minimalist warm dark
BUBBLE_EDITH = "#161616"          # Refined exhibition card
BUBBLE_NOVA = BUBBLE_EDITH        # Backward compatibility alias

