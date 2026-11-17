"""
Text-to-Speech (TTS) Engine for EDITH.

Provides asynchronous, non-blocking voice synthesis using pyttsx3.
Uses a background worker queue so the GUI thread never freezes during speech.
"""

import os
import queue
import re
import sys
import tempfile
import threading
import types
from pathlib import Path
from typing import Callable, Optional
from config import TTS_RATE, TTS_VOLUME, TTS_ENABLED_DEFAULT, DATA_DIR
from utils.logger import get_logger

logger = get_logger("tts")

# Ensure comtypes uses a local writable directory rather than restricted Roaming AppData
try:
    cache_dir = (DATA_DIR / "comtypes_cache").resolve()
    cache_dir.mkdir(parents=True, exist_ok=True)
    if "comtypes.gen" not in sys.modules:
        import comtypes
        gen_module = types.ModuleType("comtypes.gen")
        gen_module.__path__ = [str(cache_dir)]
        sys.modules["comtypes.gen"] = gen_module
        comtypes.gen = gen_module
except Exception:
    pass

try:
    import pyttsx3
    PYTTSX3_AVAILABLE = True
except ImportError:
    PYTTSX3_AVAILABLE = False
    pyttsx3 = None


def sanitize_text_for_speech(text: str) -> str:
    """
    Cleans markdown formatting, code blocks, URLs, and symbols for natural voice synthesis.
    """
    if not text:
        return ""

    # Remove markdown code blocks
    cleaned = re.sub(r"```[\s\S]*?```", " [code block omitted] ", text)
    cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)

    # Remove URLs
    cleaned = re.sub(r"https?://\S+|www\.\S+", "website link", cleaned)

    # Remove bullet markers, headers, bold/italics
    cleaned = re.sub(r"[#*_~`>|]", " ", cleaned)

    # Normalize excessive whitespace
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


class TextToSpeech:
    """
    Asynchronous Text-to-Speech manager.
    Runs speech synthesis on a dedicated background worker thread.
    """

    def __init__(
        self,
        rate: int = TTS_RATE,
        volume: float = TTS_VOLUME,
        enabled: bool = TTS_ENABLED_DEFAULT,
        on_start: Optional[Callable[[], None]] = None,
        on_finish: Optional[Callable[[], None]] = None,
    ):
        self.rate = rate
        self.volume = volume
        self.is_enabled = enabled
        self.on_start = on_start
        self.on_finish = on_finish

        self._queue = queue.Queue()
        self._stop_event = threading.Event()
        self._is_speaking = False
        self._worker_thread = None
        self._engine = None

        if PYTTSX3_AVAILABLE:
            self._start_worker()
        else:
            logger.warning("pyttsx3 is not installed. Voice output will be disabled.")

    def _init_engine(self):
        """Initializes a pyttsx3 engine instance for the current thread."""
        try:
            engine = pyttsx3.init()
            engine.setProperty("rate", self.rate)
            engine.setProperty("volume", self.volume)

            # Choose an English voice if available
            voices = engine.getProperty("voices")
            if voices:
                # Prefer female or clear English voice if found
                selected_voice = voices[0].id
                for v in voices:
                    name_lower = v.name.lower()
                    if "zira" in name_lower or "female" in name_lower or "david" in name_lower:
                        selected_voice = v.id
                        break
                engine.setProperty("voice", selected_voice)

            return engine
        except Exception as e:
            logger.error(f"Failed to initialize pyttsx3 engine: {e}")
            return None

    def _start_worker(self):
        """Spawns the background TTS consumer thread."""
        self._worker_thread = threading.Thread(
            target=self._speech_worker,
            name="EDITH_TTS_Worker",
            daemon=True
        )
        self._worker_thread.start()

    def _speech_worker(self):
        """Worker loop that dequeues and speaks text items."""
        engine = self._init_engine()

        while not self._stop_event.is_set():
            try:
                # Wait for utterance with timeout so thread can check stop_event
                item = self._queue.get(timeout=0.2)
            except queue.Empty:
                continue

            if item is None:
                # Sentinel to stop worker
                break

            if not self.is_enabled or not engine:
                self._queue.task_done()
                continue

            clean_text = sanitize_text_for_speech(item)
            if not clean_text:
                self._queue.task_done()
                continue

            try:
                self._is_speaking = True
                if self.on_start:
                    try:
                        self.on_start()
                    except Exception:
                        pass

                logger.info(f"Speaking: '{clean_text[:50]}...'")
                engine.say(clean_text)
                engine.runAndWait()

            except Exception as e:
                logger.error(f"Error during pyttsx3 speech synthesis: {e}")
                # Attempt to recreate engine if corrupted
                try:
                    engine = self._init_engine()
                except Exception:
                    pass
            finally:
                self._is_speaking = False
                if self.on_finish:
                    try:
                        self.on_finish()
                    except Exception:
                        pass
                self._queue.task_done()

    def speak(self, text: str):
        """
        Enqueues text to be spoken asynchronously.
        Does not block the calling (GUI) thread.
        """
        if not self.is_enabled or not PYTTSX3_AVAILABLE:
            return

        clean_text = text.strip()
        if clean_text:
            self._queue.put(clean_text)

    def stop(self):
        """Interrupts current speech and clears pending utterances."""
        try:
            # Drain queue
            while not self._queue.empty():
                try:
                    self._queue.get_nowait()
                    self._queue.task_done()
                except queue.Empty:
                    break

            if self._engine:
                try:
                    self._engine.stop()
                except Exception:
                    pass
        except Exception as e:
            logger.error(f"Error stopping TTS: {e}")

    def set_enabled(self, enabled: bool):
        """Enables or disables voice output."""
        self.is_enabled = bool(enabled)
        if not self.is_enabled:
            self.stop()
        logger.info(f"TTS voice output set to: {self.is_enabled}")

    def set_rate(self, rate: int):
        """Sets speaking rate (words per minute)."""
        self.rate = max(100, min(300, rate))

    def set_volume(self, volume: float):
        """Sets speaking volume (0.0 to 1.0)."""
        self.volume = max(0.0, min(1.0, volume))

    @property
    def is_speaking(self) -> bool:
        return self._is_speaking

    def shutdown(self):
        """Cleanly shuts down worker thread."""
        self._stop_event.set()
        self._queue.put(None)
