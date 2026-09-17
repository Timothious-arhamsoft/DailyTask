"""
Tests for ask_model — mock the OpenAI client; never hit Ollama or OpenAI.

A real network call would make tests slow, flaky, expensive, and dependent on
external services being up. Mocking checks our logic only.
"""

from unittest.mock import MagicMock

import pytest

from app.main import ask_model


def test_ask_model_returns_reply_text():
    """Happy path: extract the assistant text from a successful completion."""
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices = [
        MagicMock(message=MagicMock(content="a real-looking reply"))
    ]

    result = ask_model(fake_client, model="test-model", message="hello")

    assert result == "a real-looking reply"
    fake_client.chat.completions.create.assert_called_once_with(
        model="test-model",
        messages=[{"role": "user", "content": "hello"}],
    )


def test_ask_model_propagates_a_real_client_error():
    """Error path: connection failures must bubble up to the caller."""
    fake_client = MagicMock()
    fake_client.chat.completions.create.side_effect = ConnectionError(
        "local server not running"
    )

    with pytest.raises(ConnectionError, match="local server not running"):
        ask_model(fake_client, model="test-model", message="hello")


def test_ask_model_handles_none_content():
    """Edge case: if the API returns null content, return an empty string."""
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value.choices = [
        MagicMock(message=MagicMock(content=None))
    ]

    result = ask_model(fake_client, model="test-model", message="hello")

    assert result == ""
