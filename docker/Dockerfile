# syntax=docker/dockerfile:1.12

# Choose a python version that you know works with your application
FROM python:3.12-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.5.15 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Combine layers and use --link for improved caching
COPY --link pyscribble ./pyscribble/
COPY --link requirements.txt app.py ./

# Combine RUN commands to reduce layers
RUN uv pip install --no-cache-dir -r requirements.txt && \
    uv pip install --no-cache-dir marimo && \
    rm requirements.txt

# Create non-root user in a single RUN command
RUN useradd -m app_user && \
    chown -R app_user:app_user /app

USER app_user

# Use EXPOSE for documentation, not functional networking
EXPOSE 8080

CMD [ "marimo", "run", "app.py", "--host", "0.0.0.0", "-p", "8080" ]
