"""
FastAPI service wrapping local + hosted chat models behind one contract.

Both /chat/local and /chat/hosted call the same ask_model() function.
Only the OpenAI-compatible client (base_url + api_key) and model name differ.
Swap providers by changing .env — no code changes required.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)

app = FastAPI(
    title="Week 07 · Local + Hosted Chat",
    description="One OpenAI-compatible client; local or hosted via env config.",
    version="1.0.0",
)


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, description="User message to send to the model")


class ChatResponse(BaseModel):
    reply: str


def _reload_env() -> None:
    """Re-read .env so HOSTED_* / LOCAL_* edits apply without a full rethink."""
    load_dotenv(Path(__file__).resolve().parent.parent / ".env", override=True)


def _env(name: str, default: str | None = None) -> str | None:
    _reload_env()
    value = os.getenv(name, default)
    if value is None:
        return None
    value = value.strip()
    return value or None


def get_client(use_local: bool) -> OpenAI:
    """
    Build an OpenAI-compatible client for local or hosted inference.

    Reads env at call time so .env edits apply after process restart
    (or on the next request if you restarted uvicorn).
    """
    if use_local:
        base_url = _env("LOCAL_BASE_URL", "http://localhost:11434/v1")
        api_key = _env("LOCAL_API_KEY", "ollama") or "ollama"
        return OpenAI(base_url=base_url, api_key=api_key)

    base_url = _env("HOSTED_BASE_URL")
    api_key = _env("HOSTED_API_KEY")
    if not base_url:
        raise RuntimeError(
            "HOSTED_BASE_URL is not set. Example for Groq: "
            "https://api.groq.com/openai/v1"
        )
    if not api_key:
        raise RuntimeError(
            "HOSTED_API_KEY is not set. Put it in Task29/.env (never hardcode it)."
        )
    return OpenAI(base_url=base_url, api_key=api_key)


def ask_model(client: OpenAI, model: str, message: str) -> str:
    """
    Shared model-calling logic. Does not know or care which provider
    `client` points at — local laptop or a hosted API.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}],
    )
    content = response.choices[0].message.content
    return content if content is not None else ""


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/chat/local", response_model=ChatResponse)
def chat_local(payload: ChatRequest) -> ChatResponse:
    """Wrap a local model (e.g. Ollama) behind our request/response contract."""
    model = _env("LOCAL_MODEL", "llama3.2:3b") or "llama3.2:3b"
    try:
        client = get_client(use_local=True)
        reply = ask_model(client, model=model, message=payload.message)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return ChatResponse(reply=reply)


@app.post("/chat/hosted", response_model=ChatResponse)
def chat_hosted(payload: ChatRequest) -> ChatResponse:
    """Same contract as /chat/local; provider chosen via HOSTED_* env vars."""
    # Groq free-tier friendly default (Llama IDs may be restricted on some accounts).
    model = _env("HOSTED_MODEL", "openai/gpt-oss-20b") or "openai/gpt-oss-20b"
    try:
        client = get_client(use_local=False)
        reply = ask_model(client, model=model, message=payload.message)
    except Exception as exc:  
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return ChatResponse(reply=reply)
