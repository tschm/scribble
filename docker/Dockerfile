# syntax=docker/dockerfile:1.12

# Choose a python version that you know works with your application
FROM python:3.12-slim

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.5.15 /uv /bin/uv
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Combine layers and use --link for improved caching
RUN mkdir -p /app/pyscribble

#COPY requirements.txt /app/
COPY . .
RUN ls -all

# Combine RUN commands to reduce layers
RUN uv pip install --no-cache-dir -r /app/requirements.txt && \
    uv pip install --no-cache-dir marimo && \
    rm requirements.txt

COPY pyscribble /app/pyscribble
COPY app.py /app/

# Create non-root user in a single RUN command
RUN useradd -m app_user && \
    chown -R app_user:app_user /app

USER app_user

# Use EXPOSE for documentation, not functional networking
EXPOSE 8080

CMD [ "marimo", "run", "app.py", "--host", "0.0.0.0", "-p", "8080" ]
