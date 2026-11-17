"""
AI Engine Module for EDITH.

Integrates Google's official `google-genai` Python SDK to provide
context-aware conversational AI responses.
Handles missing keys gracefully without crashing.
"""

import os
from typing import Optional
from dotenv import load_dotenv

# Import Google GenAI SDK
try:
    from google import genai
    from google.genai import types, errors
    GENAI_AVAILABLE = True
except ImportError:
    GENAI_AVAILABLE = False
    genai = None
    types = None
    errors = None

import config
from utils.logger import get_logger

logger = get_logger("ai_engine")

EDITH_SYSTEM_INSTRUCTION = (
    "You are EDITH (Even Dead, I'm The Hero), an intelligent, highly capable, and polite desktop virtual assistant "
    "designed for an Artificial Intelligence Lab project. "
    "Provide clear, accurate, and concise answers suitable for voice or chat reading "
    "(typically 2 to 3 sentences unless the user explicitly requests code, step-by-step instructions, or in-depth technical detail). "
    "Never speak rudely. Keep responses natural, helpful, direct, and conversational."
)
NOVA_SYSTEM_INSTRUCTION = EDITH_SYSTEM_INSTRUCTION

class AIEngine:
    """
    Manages communication with Google's Gemini API via the official google-genai SDK.
    Maintains session chat history for multi-turn conversational context.
    """

    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        self.api_key = (api_key if api_key is not None else config.get_gemini_api_key()).strip()
        self.model_name = (model if model is not None else config.get_gemini_model()).strip() or "gemini-2.5-flash"
        self.client = None
        self.chat_session = None
        self._initialize_client()

    def reload_config(self) -> bool:
        """
        Reloads environment variables from .env to detect newly added API keys.
        """
        if config.ENV_FILE.exists():
            load_dotenv(dotenv_path=config.ENV_FILE, override=True)
        self.api_key = config.get_gemini_api_key()
        self.model_name = config.get_gemini_model()
        return self._initialize_client()

    def _initialize_client(self) -> bool:
        """
        Initializes the GenAI client and begins a conversational chat session.
        """
        if not GENAI_AVAILABLE:
            logger.warning("google-genai package is not available in current environment.")
            self.client = None
            self.chat_session = None
            return False

        if not self.is_configured():
            logger.info("Gemini API key is not configured. Running in built-in offline mode.")
            self.client = None
            self.chat_session = None
            return False

        try:
            self.client = genai.Client(api_key=self.api_key)
            self._start_new_chat()
            logger.info(f"Gemini client initialized with model '{self.model_name}'.")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Gemini Client: {e}")
            self.client = None
            self.chat_session = None
            return False

    def _start_new_chat(self):
        """Initializes or resets a multi-turn chat session with system instruction."""
        if not self.client:
            return

        try:
            # Official google-genai SDK chats interface
            config_params = {}
            if hasattr(types, "GenerateContentConfig"):
                config_params["config"] = types.GenerateContentConfig(
                    system_instruction=NOVA_SYSTEM_INSTRUCTION,
                    temperature=0.7,
                    max_output_tokens=500
                )

            self.chat_session = self.client.chats.create(
                model=self.model_name,
                **config_params
            )
            logger.info("New multi-turn chat session started.")
        except Exception as e:
            logger.warning(f"Could not create chat session with system instruction: {e}. Falling back to default chat.")
            try:
                self.chat_session = self.client.chats.create(model=self.model_name)
            except Exception as inner_e:
                logger.error(f"Chat session creation failed completely: {inner_e}")
                self.chat_session = None

    def is_configured(self) -> bool:
        """
        Returns True if a valid API key appears to be configured.
        """
        key = self.api_key.strip()
        if not key or key == "YOUR_GEMINI_API_KEY_HERE" or key.startswith("YOUR_"):
            return False
        return len(key) >= 15

    def reset_chat(self):
        """Resets conversational memory for a fresh session."""
        if self.is_configured() and self.client:
            self._start_new_chat()

    def generate_response(self, user_prompt: str) -> str:
        """
        Sends user message to Gemini and returns conversational response.
        If the API key is not configured or an error occurs, returns safe fallback.
        """
        if not self.is_configured():
            return "AI mode is not configured. Please add your Gemini API key to the .env file."

        if not GENAI_AVAILABLE:
            return "google-genai SDK is not installed. Please check requirements.txt."

        # Re-initialize client if not active
        if not self.client or not self.chat_session:
            success = self._initialize_client()
            if not success or not self.chat_session:
                return "AI mode is not configured. Please add your Gemini API key to the .env file."

        try:
            logger.info(f"Sending prompt to Gemini ({self.model_name}): '{user_prompt[:50]}...'")
            response = self.chat_session.send_message(user_prompt)

            if not response or not response.text:
                return "I received an empty response from the AI service. Please try asking again."

            response_text = response.text.strip()
            logger.info(f"Gemini response received ({len(response_text)} chars).")
            return response_text

        except Exception as exc:
            err_str = str(exc)
            logger.error(f"Gemini API Error: {err_str}")

            # Specific diagnostic error messages
            if "API_KEY_INVALID" in err_str or ("400" in err_str and "key" in err_str.lower()) or "invalid api key" in err_str.lower():
                return (
                    "Your Gemini API key in .env appears to be invalid. "
                    "Google Gemini API keys start with 'AIzaSy' and can be created for free at https://aistudio.google.com/. "
                    "Meanwhile, all built-in commands (notes, calculator, time/date, apps) work normally!"
                )
            elif "429" in err_str or "RESOURCE_EXHAUSTED" in err_str or "quota" in err_str.lower():
                return "The Gemini API quota limit has been reached. Please wait a moment or check your Google AI Studio plan."
            elif "404" in err_str or "NOT_FOUND" in err_str or "model" in err_str.lower():
                return f"The model '{self.model_name}' was not found. Please set GEMINI_MODEL=gemini-2.5-flash in your .env file."
            elif any(k in err_str.lower() for k in ["connection", "network", "timeout", "getaddrinfo", "11001", "name resolution", "dns"]):
                return "I could not reach Google's AI servers. Please check your internet connection."
            else:
                return f"AI service encountered an issue: {err_str[:120]}. Please try again."

    def get_status_info(self) -> dict:
        """Returns diagnostic info about AI engine state."""
        return {
            "configured": self.is_configured(),
            "model": self.model_name,
            "sdk_available": GENAI_AVAILABLE,
            "has_active_session": bool(self.chat_session is not None),
        }

