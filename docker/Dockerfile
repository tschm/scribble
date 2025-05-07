# syntax=docker/dockerfile:1.15
FROM python:3.13-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.7.3 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Create non-root user early
RUN useradd -m app_user && \
    chown app_user:app_user /app

# Copy and install dependencies first for better caching
COPY --chown=app_user:app_user requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=app_user:app_user . .

# Switch to non-root user
USER app_user

EXPOSE 8080

CMD ["marimo", "run", "app.py", "--host", "0.0.0.0", "-p", "8080"]
