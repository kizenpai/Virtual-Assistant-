"""
Assistant Coordinator Module for EDITH.

Implements the smart command router, integrates the AI Engine,
Speech Recognition, Text-to-Speech, and built-in automation into a unified assistant.
"""

from typing import Any, Callable, Dict, Optional
import config
from core.ai_engine import AIEngine
from core.command_handler import CommandHandler
from core.speech_to_text import SpeechToText
from core.text_to_speech import TextToSpeech
from utils.logger import get_logger

logger = get_logger("assistant")

class EdithAssistant:
    """
    Main virtual assistant class. Coordinates input routing, TTS, STT, and AI engine.
    """

    def __init__(
        self,
        on_status_change: Optional[Callable[[str, str], None]] = None,
        on_speech_start: Optional[Callable[[], None]] = None,
        on_speech_finish: Optional[Callable[[], None]] = None,
    ):
        self.on_status_change = on_status_change
        self.on_speech_start = on_speech_start
        self.on_speech_finish = on_speech_finish

        # Initialize sub-components
        logger.info("Initializing EDITH components...")
        self.command_handler = CommandHandler()
        self.ai_engine = AIEngine()
        self.stt = SpeechToText()
        self.tts = TextToSpeech(
            rate=config.TTS_RATE,
            volume=config.TTS_VOLUME,
            enabled=config.TTS_ENABLED_DEFAULT,
            on_start=self._handle_speech_start,
            on_finish=self._handle_speech_finish,
        )

        self.last_status = "Online"
        self._notify_status("Online", config.STATUS_ONLINE)

    def _notify_status(self, status: str, color_hex: str):
        """Dispatches status updates to UI listener."""
        self.last_status = status
        if self.on_status_change:
            try:
                self.on_status_change(status, color_hex)
            except Exception as e:
                logger.error(f"Status notification callback error: {e}")

    def _handle_speech_start(self):
        """Invoked when TTS begins speaking."""
        self._notify_status("Speaking", config.STATUS_SPEAKING)
        if self.on_speech_start:
            try:
                self.on_speech_start()
            except Exception:
                pass

    def _handle_speech_finish(self):
        """Invoked when TTS completes utterance."""
        self._notify_status("Online", config.STATUS_ONLINE)
        if self.on_speech_finish:
            try:
                self.on_speech_finish()
            except Exception:
                pass

    def process_input(self, user_text: str) -> Dict[str, Any]:
        """
        Smart Command Routing Pipeline:
        1. Receive user input and check built-in commands first.
        2. If matched, return built-in result.
        3. If unmatched (is_ai_candidate), route to Gemini AI engine.
        4. If AI is unconfigured or fails, provide the fallback response.
        5. Trigger TTS speech if enabled and appropriate.
        """
        clean_text = user_text.strip()
        if not clean_text:
            return {
                "user_text": "",
                "response": "Please enter a command or ask a question.",
                "source": "system",
                "should_exit": False,
            }

        logger.info(f"Processing input: '{clean_text}'")
        self._notify_status("Processing", config.STATUS_PROCESSING)

        # Step 1: Check built-in commands
        cmd_result = self.command_handler.handle(clean_text)

        if cmd_result.get("matched"):
            response_text = cmd_result.get("response", "")
            source = "built-in"
            should_exit = cmd_result.get("should_exit", False)

        elif cmd_result.get("is_ai_candidate"):
            # Step 2: Route to Gemini AI
            logger.info("Routing unmatched query to Gemini AI...")
            if not self.ai_engine.is_configured():
                response_text = "AI mode is not configured. Please add your Gemini API key to the .env file."
                source = "ai_unconfigured"
            else:
                response_text = self.ai_engine.generate_response(clean_text)
                source = "gemini"
            should_exit = False

        else:
            response_text = "I didn't quite understand that. You can type 'help' to see what I can do."
            source = "system"
            should_exit = False

        # Step 3: Trigger Text-to-Speech
        if cmd_result.get("speak", True) and response_text:
            self.tts.speak(response_text)

        self._notify_status("Online", config.STATUS_ONLINE)

        return {
            "user_text": clean_text,
            "response": response_text,
            "source": source,
            "action": cmd_result.get("action"),
            "should_exit": should_exit,
        }

    def listen_and_process(self) -> Dict[str, Any]:
        """
        Captures single voice input via STT and processes through the pipeline.
        Must be called from a worker thread to keep GUI responsive.
        """
        self._notify_status("Listening", config.STATUS_LISTENING)
        success, text_or_err = self.stt.listen_once()

        if not success:
            self._notify_status("Online", config.STATUS_ONLINE)
            return {
                "user_text": "",
                "response": text_or_err,
                "source": "stt_error",
                "should_exit": False,
            }

        return self.process_input(text_or_err)

    def set_speech_enabled(self, enabled: bool):
        """Toggles voice synthesis on/off."""
        self.tts.set_enabled(enabled)

    def stop_speaking(self):
        """Immediately halts active speech."""
        self.tts.stop()

    def reload_ai_config(self) -> bool:
        """Reloads Gemini API key from environment."""
        return self.ai_engine.reload_config()

    def shutdown(self):
        """Cleans up threads and engines on exit."""
        logger.info("Shutting down EDITH Assistant...")
        self.tts.shutdown()
        self._notify_status("Offline", config.STATUS_OFFLINE)

# Backward-compatibility alias
NovaAssistant = EdithAssistant

