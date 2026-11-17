"""
Unit tests for command handler module.
"""

from unittest.mock import patch, MagicMock
import pytest
from core.command_handler import CommandHandler

@pytest.fixture
def handler():
    return CommandHandler()

def test_greeting_commands(handler):
    res_hello = handler.handle("hello")
    assert res_hello["matched"] is True
    assert "EDITH" in res_hello["response"] or "NOVA" in res_hello["response"]

    res_morning = handler.handle("good morning")
    assert res_morning["matched"] is True
    assert "morning" in res_morning["response"].lower()

    res_how_are_you = handler.handle("how are you?")
    assert res_how_are_you["matched"] is True
    assert "functioning" in res_how_are_you["response"].lower()

def test_date_and_time_commands(handler):
    res_time = handler.handle("what time is it?")
    assert res_time["matched"] is True
    assert "time is" in res_time["response"].lower()

    res_date = handler.handle("what is today's date?")
    assert res_date["matched"] is True
    assert "today is" in res_date["response"].lower()

def test_joke_command(handler):
    res_joke = handler.handle("tell me a joke")
    assert res_joke["matched"] is True
    assert len(res_joke["response"]) > 10

def test_help_command(handler):
    res_help = handler.handle("help")
    assert res_help["matched"] is True
    assert res_help["action"] == "SHOW_HELP"
    assert "Commands" in res_help["response"] or "commands" in res_help["response"]

def test_exit_command(handler):
    res_exit = handler.handle("exit")
    assert res_exit["matched"] is True
    assert res_exit["should_exit"] is True
    assert "Goodbye" in res_exit["response"]

@patch("webbrowser.open")
def test_open_youtube(mock_web, handler):
    res = handler.handle("open youtube")
    assert res["matched"] is True
    assert res["action"] == "OPEN_YOUTUBE"
    mock_web.assert_called_once_with("https://www.youtube.com")

@patch("webbrowser.open")
def test_open_google(mock_web, handler):
    res = handler.handle("open google")
    assert res["matched"] is True
    assert res["action"] == "OPEN_GOOGLE"
    mock_web.assert_called_once_with("https://www.google.com")

@patch("webbrowser.open")
def test_open_github(mock_web, handler):
    res = handler.handle("open github")
    assert res["matched"] is True
    assert res["action"] == "OPEN_GITHUB"
    mock_web.assert_called_once_with("https://github.com")

@patch("webbrowser.open")
def test_open_custom_website(mock_web, handler):
    res = handler.handle("open website github.com")
    assert res["matched"] is True
    assert res["action"] == "OPEN_WEBSITE"
    mock_web.assert_called_once_with("https://github.com")

@patch("webbrowser.open")
def test_google_search(mock_web, handler):
    res = handler.handle("search google for artificial intelligence")
    assert res["matched"] is True
    assert res["action"] == "GOOGLE_SEARCH"
    assert "artificial intelligence" in res["response"]
    assert mock_web.called

@patch("wikipedia.summary")
def test_wikipedia_summary(mock_wiki, handler):
    mock_wiki.return_value = "Alan Turing was an English mathematician and computer scientist."
    res = handler.handle("wikipedia Alan Turing")
    assert res["matched"] is True
    assert "According to Wikipedia" in res["response"]
    assert "Alan Turing" in res["response"]

@patch("subprocess.Popen")
def test_open_notepad(mock_popen, handler):
    res = handler.handle("open notepad")
    assert res["matched"] is True
    assert res["action"] == "OPEN_NOTEPAD"
    mock_popen.assert_called_once_with(["notepad.exe"])

@patch("subprocess.Popen")
def test_open_calculator(mock_popen, handler):
    res = handler.handle("open calculator")
    assert res["matched"] is True
    assert res["action"] == "OPEN_CALC"
    mock_popen.assert_called_once_with(["calc.exe"])

def test_unmatched_routes_to_ai(handler):
    res = handler.handle("explain how quantum computing works in detail")
    assert res["matched"] is False
    assert res["is_ai_candidate"] is True

