"""
Unit tests for notes manager module.
"""

import pytest
from pathlib import Path
from utils.notes_manager import save_note, read_notes, get_notes_formatted, clear_notes

@pytest.fixture(autouse=True)
def clean_notes_before_test():
    """Ensure notes are clean before each test runs."""
    clear_notes()
    yield
    clear_notes()

def test_save_and_read_note():
    success, msg = save_note("Submit AI Lab Project on Monday")
    assert success is True
    assert "saved" in msg.lower()

    notes = read_notes()
    assert len(notes) == 1
    assert "Submit AI Lab Project on Monday" in notes[0]

def test_save_empty_note():
    success, msg = save_note("   ")
    assert success is False
    assert "cannot be empty" in msg

def test_multiple_notes():
    save_note("First task")
    save_note("Second task")
    notes = read_notes()
    assert len(notes) == 2
    assert "First task" in notes[0]
    assert "Second task" in notes[1]

def test_get_notes_formatted():
    save_note("Buy components")
    formatted = get_notes_formatted()
    assert "You have 1 saved note" in formatted
    assert "1. " in formatted
    assert "Buy components" in formatted

def test_clear_notes():
    save_note("Temporary note")
    assert len(read_notes()) == 1

    success, msg = clear_notes()
    assert success is True
    assert len(read_notes()) == 0
    assert "no saved notes" in get_notes_formatted()

