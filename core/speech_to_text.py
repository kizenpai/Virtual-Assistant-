"""
Speech-to-Text (STT) Module for EDITH.

Captures microphone audio and converts it to text using SpeechRecognition.
Provides robust handling for timeouts, unrecognized audio, device selection, and ambient noise.
"""

from typing import Optional, Tuple
from config import STT_ENERGY_THRESHOLD, STT_LISTEN_TIMEOUT, STT_PHRASE_TIME_LIMIT
from utils.logger import get_logger

logger = get_logger("stt")

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    sr = None

try:
    import pyaudio
    PYAUDIO_AVAILABLE = True
except ImportError:
    PYAUDIO_AVAILABLE = False
    pyaudio = None


class SpeechToText:
    """
    Manages audio capture from microphone and speech recognition.
    """

    def __init__(self):
        self.recognizer = None
        self._microphone_available = False
        self._preferred_device_index = None

        if SR_AVAILABLE:
            self.recognizer = sr.Recognizer()
            self.recognizer.energy_threshold = STT_ENERGY_THRESHOLD
            self.recognizer.dynamic_energy_threshold = True
            self.recognizer.dynamic_energy_adjustment_damping = 0.15
            self.recognizer.dynamic_energy_ratio = 1.3
            self.recognizer.pause_threshold = 0.8
            self.recognizer.non_speaking_duration = 0.4
            self._check_microphone()
        else:
            logger.warning("SpeechRecognition library not available.")

    def _check_microphone(self) -> bool:
        """Verifies whether at least one audio input device exists."""
        if not SR_AVAILABLE:
            self._microphone_available = False
            return False

        try:
            mic_list = sr.Microphone.list_microphone_names()
            if not mic_list:
                self._microphone_available = False
                logger.warning("No microphone input devices detected.")
                return False

            self._microphone_available = True
            logger.info(f"Detected {len(mic_list)} microphone device(s).")

            # Check for preferred working device
            if PYAUDIO_AVAILABLE:
                try:
                    p = pyaudio.PyAudio()
                    for i in range(p.get_device_count()):
                        dev = p.get_device_info_by_index(i)
                        name = dev.get("name", "").lower()
                        if dev.get("maxInputChannels", 0) > 0:
                            # Prioritize default or dedicated microphone array
                            if "realtek" in name or "microphone" in name or "mapper" in name:
                                self._preferred_device_index = i
                                break
                    p.terminate()
                except Exception:
                    self._preferred_device_index = None

            return True
        except Exception as e:
            logger.warning(f"Microphone detection error: {e}")
            self._microphone_available = False
            return False

    def is_available(self) -> bool:
        """Returns True if STT library and microphone are ready."""
        return SR_AVAILABLE and self._microphone_available

    def _get_mic_instance(self):
        """Returns a microphone instance, preferring an active input device."""
        if self._preferred_device_index is not None:
            try:
                return sr.Microphone(device_index=self._preferred_device_index)
            except Exception:
                pass
        return sr.Microphone()

    def listen_once(
        self,
        timeout: int = STT_LISTEN_TIMEOUT,
        phrase_time_limit: int = STT_PHRASE_TIME_LIMIT
    ) -> Tuple[bool, str]:
        """
        Listens to the microphone for an utterance and converts to text.

        Returns:
            (success: bool, text_or_error_message: str)
        """
        if not SR_AVAILABLE:
            return False, "Speech recognition library is not installed. You can still use the text input below."

        try:
            mic = self._get_mic_instance()
            with mic as source:
                logger.info("Calibrating for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.3)

                logger.info("Listening for user speech...")
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

            logger.info("Processing captured audio...")
            recognized_text = self.recognizer.recognize_google(audio)
            clean_text = recognized_text.strip()
            logger.info(f"Speech recognized: '{clean_text}'")
            return True, clean_text

        except sr.WaitTimeoutError:
            logger.info("Speech recognition timed out (no speech detected).")
            return False, "I didn't hear anything. Please press the 🎤 Microphone button and speak clearly."

        except sr.UnknownValueError:
            logger.info("Google Speech Recognition could not understand audio.")
            return False, "I couldn't quite understand what you said. Please try speaking closer to your microphone."

        except sr.RequestError as e:
            logger.error(f"Speech recognition network/service error: {e}")
            return False, "Could not reach speech recognition servers. Please check your internet connection or use text input."

        except (OSError, AttributeError) as e:
            logger.error(f"Microphone access error: {e}")
            self._microphone_available = False
            return False, "Microphone access issue. Please check your microphone settings or use text input."

        except Exception as e:
            logger.error(f"Unexpected STT error: {e}")
            return False, f"Listening error: {e}"
