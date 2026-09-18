# Task 29 — Local and Hosted LLM Chat API

## Running the Application

From the `Task29` directory (where the `app` package is located), run:

```bash
uvicorn app.main:app --reload
```
---

## Overview
This task implements a FastAPI service that provides a unified interface for interacting with both local and hosted Large Language Models (LLMs). Both chat endpoints utilize a shared `ask_model()` function to deliver a consistent response structure. Provider settings, credentials, and model names are completely configurable via environment variables.

---

## Project Structure

```text
Task29/
├── app/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_ask_model.py
├── peft_lora_explanation.md
├── requirements.txt
└── README.md
```

---

## Setup & Installation

### 1. Navigate to the Task29 Directory
```bash
cd ~/Downloads/Repos/DailyTask/Task29
```

### 2. Activate the Virtual Environment
If your virtual environment already exists:
```bash
source .venv/bin/activate
```

If you need to create a new virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `Task29` directory and configure your provider settings:

```env
# Local model configuration
LOCAL_BASE_URL=http://localhost:11434/v1
LOCAL_API_KEY=ollama
LOCAL_MODEL=llama3.2:3b

# Hosted model configuration
HOSTED_BASE_URL=your_hosted_provider_base_url
HOSTED_API_KEY=your_hosted_api_key
HOSTED_MODEL=your_hosted_model_name
```
> **Note:** Replace the hosted placeholders with actual provider values. Keep API keys secure and never commit `.env` files to public repositories.

---

### Available Services:
* **API Base:** `http://127.0.0.1:8000`
* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **Health Check:** `http://127.0.0.1:8000/health`

---

## API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Checks whether the FastAPI application is running. |
| `POST` | `/chat/local` | Sends a message to the configured local model. |
| `POST` | `/chat/hosted` | Sends a message to the configured hosted model. |

### Example Request
```json
{
  "message": "Explain machine learning in simple words."
}
```

### Example Response
```json
{
  "reply": "Machine learning is a way for computers to learn patterns from data..."
}
```

---

## Local Model Requirements

The local endpoint defaults to an **Ollama-compatible API**. Ensure Ollama is installed, active, and the designated model is pulled locally:

```bash
ollama pull llama3.2:3b
```

---

## Running Tests

To run all tests from the `Task29` directory:
```bash
pytest
```

To target the `ask_model()` test module specifically:
```bash
pytest tests/test_ask_model.py
```

---

## PEFT and LoRA

The included `peft_lora_explanation.md` file contains a detailed explanation of Parameter-Efficient Fine-Tuning (PEFT) and Low-Rank Adaptation (LoRA).

---

## Notes
* **Shared Logic:** Both local and hosted endpoints leverage identical underlying model-calling logic.
* **Environment-Driven:** All URLs, keys, and model target names are strictly driven by environment variables.
* **Health Check Scope:** The `/health` endpoint validates API readiness, not external model provider availability.