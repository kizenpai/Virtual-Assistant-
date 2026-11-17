"""
Notes Manager Module for NOVA.

Manages saving, reading, formatting, and clearing notes stored in data/notes.txt.
"""

from datetime import datetime
from pathlib import Path
from typing import List, Tuple
from config import NOTES_FILE, DATA_DIR
from utils.logger import get_logger

logger = get_logger("notes_manager")

def _ensure_file():
    """Ensure data directory and notes file exist."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not NOTES_FILE.exists():
        NOTES_FILE.touch()

def save_note(note_text: str) -> Tuple[bool, str]:
    """
    Appends a new note with a timestamp to data/notes.txt.
    """
    clean_text = note_text.strip()
    if not clean_text:
        return False, "Note content cannot be empty."

    try:
        _ensure_file()
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p")
        formatted_entry = f"[{timestamp}] {clean_text}\n"

        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(formatted_entry)

        logger.info(f"Note successfully saved: '{clean_text[:40]}...'")
        return True, f"I have saved your note: \"{clean_text}\""

    except Exception as e:
        logger.error(f"Failed to save note: {e}")
        return False, f"Could not save the note due to an error: {e}"

def read_notes() -> List[str]:
    """
    Reads all non-empty note lines from data/notes.txt.
    """
    _ensure_file()
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        return lines
    except Exception as e:
        logger.error(f"Failed to read notes: {e}")
        return []

def get_notes_formatted() -> str:
    """
    Returns a nicely formatted string of all notes for display and voice output.
    """
    notes = read_notes()
    if not notes:
        return "You have no saved notes."

    formatted = [f"You have {len(notes)} saved note{'s' if len(notes) > 1 else ''}:"]
    for idx, note in enumerate(notes, start=1):
        formatted.append(f"{idx}. {note}")

    return "\n".join(formatted)

def clear_notes() -> Tuple[bool, str]:
    """
    Clears all saved notes from data/notes.txt.
    """
    try:
        _ensure_file()
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("# NOVA Virtual Assistant Notes File\n")
        logger.info("All notes cleared.")
        return True, "All your saved notes have been cleared."
    except Exception as e:
        logger.error(f"Failed to clear notes: {e}")
        return False, f"Failed to clear notes: {e}"

def delete_note_by_index(index: int) -> Tuple[bool, str]:
    """
    Deletes a specific note by its 1-based index.
    """
    notes = read_notes()
    if not notes:
        return False, "You have no notes to delete."

    if index < 1 or index > len(notes):
        return False, f"Invalid note index #{index}. You have {len(notes)} note(s)."

    try:
        removed = notes.pop(index - 1)
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("# NOVA Virtual Assistant Notes File\n")
            for n in notes:
                f.write(f"{n}\n")
        return True, f"Deleted note: {removed}"
    except Exception as e:
        logger.error(f"Failed to delete note index {index}: {e}")
        return False, f"Error deleting note: {e}"

