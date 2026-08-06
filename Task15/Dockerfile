FROM python:3.12-slim

WORKDIR /app

# Dependencies first — this layer is only invalidated when requirements.txt
# changes, so routine app code edits reuse the cached pip install layer.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App code last — the layer that changes most often, kept as late as possible.
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]