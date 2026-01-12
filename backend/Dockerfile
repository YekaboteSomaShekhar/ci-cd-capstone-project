# ---- Build Stage ----
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Runtime Stage ----
FROM python:3.11-slim
WORKDIR /app

RUN useradd -m appuser
USER appuser

COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY app.py .

EXPOSE 5000
CMD ["python", "app.py"]
