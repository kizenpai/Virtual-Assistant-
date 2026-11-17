"""
Logging module for NOVA.

Provides thread-safe logging to both console and rotating log file.
Ensures sensitive tokens (like Gemini API keys) are sanitized before logging.
"""

import logging
import os
import re
from logging.handlers import RotatingFileHandler
from pathlib import Path
from config import LOGS_DIR

# Masking pattern for API keys
API_KEY_PATTERN = re.compile(r"AIza[0-9A-Za-z\-_]{35}")

class SensitiveDataFilter(logging.Filter):
    """Filter that masks API keys and sensitive tokens in log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        if isinstance(record.msg, str):
            record.msg = API_KEY_PATTERN.sub("[MASKED_API_KEY]", record.msg)
        return True

def setup_logger(name: str = "nova", level: int = logging.INFO) -> logging.Logger:
    """
    Configures and returns a logger instance with console and file handlers.
    """
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    logger.setLevel(level)
    logger.propagate = False

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s:%(funcName)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    sensitive_filter = SensitiveDataFilter()

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    console_handler.addFilter(sensitive_filter)
    logger.addHandler(console_handler)

    # File Handler
    try:
        log_file = LOGS_DIR / "nova.log"
        file_handler = RotatingFileHandler(
            filename=str(log_file),
            maxBytes=2 * 1024 * 1024,  # 2 MB per file
            backupCount=3,
            encoding="utf-8"
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        file_handler.addFilter(sensitive_filter)
        logger.addHandler(file_handler)
    except Exception as e:
        print(f"[Logger Warning] Could not attach file handler: {e}")

    return logger

def get_logger(name: str = "nova") -> logging.Logger:
    """Retrieve an existing logger or create a new one."""
    return setup_logger(name)

