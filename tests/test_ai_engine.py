"""
Unit tests for AI Engine module and Gemini integration.
"""

from unittest.mock import MagicMock, patch
import pytest
from core.ai_engine import AIEngine

def test_ai_engine_unconfigured_default():
    engine = AIEngine(api_key="", model="gemini-2.5-flash")
    assert engine.is_configured() is False

    response = engine.generate_response("What is the capital of France?")
    assert response == "AI mode is not configured. Please add your Gemini API key to the .env file."

def test_ai_engine_placeholder_key():
    engine = AIEngine(api_key="YOUR_GEMINI_API_KEY_HERE")
    assert engine.is_configured() is False

    response = engine.generate_response("Tell me about space exploration")
    assert response == "AI mode is not configured. Please add your Gemini API key to the .env file."

def test_ai_engine_status_info():
    engine = AIEngine(api_key="")
    status = engine.get_status_info()
    assert status["configured"] is False
    assert "model" in status
    assert status["sdk_available"] is True

@patch("core.ai_engine.genai.Client")
def test_ai_engine_configured_mocked(mock_client_cls):
    mock_client = MagicMock()
    mock_chat = MagicMock()
    mock_resp = MagicMock()
    mock_resp.text = "Paris is the capital of France."
    mock_chat.send_message.return_value = mock_resp
    mock_client.chats.create.return_value = mock_chat
    mock_client_cls.return_value = mock_client

    engine = AIEngine(api_key="AIzaSyMockKeyForTestingPurposes12345", model="gemini-2.5-flash")
    assert engine.is_configured() is True

    answer = engine.generate_response("What is the capital of France?")
    assert answer == "Paris is the capital of France."

