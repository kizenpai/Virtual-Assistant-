"""Utilities package for NOVA Virtual Assistant."""

from utils.logger import setup_logger, get_logger
from utils.calculator import calculate
from utils.notes_manager import (
    save_note,
    read_notes,
    get_notes_formatted,
    clear_notes,
    delete_note_by_index
)

__all__ = [
    "setup_logger",
    "get_logger",
    "calculate",
    "save_note",
    "read_notes",
    "get_notes_formatted",
    "clear_notes",
    "delete_note_by_index",
]

