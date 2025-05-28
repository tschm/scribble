# syntax=docker/dockerfile:1.16
FROM python:3.13-slim AS base

# Install uv for fast package management
COPY --from=ghcr.io/astral-sh/uv:0.7.8 /uv /bin/uv

# Set environment variables in one layer
# Combining multiple ENV commands into one reduces the number of layers in the final image
ENV PATH="/home/user/.local/bin:$PATH" \
    UV_SYSTEM_PYTHON=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Explanation of environment variables:
# - PATH: Adds user's local bin to the PATH to find executables installed with --user
# - UV_SYSTEM_PYTHON=1: Tells uv to use the system Python instead of creating a virtual environment
# - PYTHONUNBUFFERED=1: Prevents Python from buffering stdout/stderr (better for logging in containers)
# - PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files (reduces image size)
# - PIP_NO_CACHE_DIR=1: Prevents pip from using a cache directory (reduces image size)

# Create non-root user and chown the app directory
# Running as a non-root user is a security best practice for containers
# - useradd -m: Creates a user with a home directory
# - -u 1000: Sets the user ID to 1000 (standard for first non-root user)
# - mkdir /app: Creates the application directory
# - chown user:user /app: Gives the new user ownership of the app directory
RUN useradd -m -u 1000 user && mkdir /app && chown user:user /app

WORKDIR /app

# Copy and install dependencies first for better caching
COPY --chown=user:user requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt

# Copy the pyscribble package to the container
# This contains the core functionality for the pyscribble application
COPY --chown=user:user ./pyscribble .

# Copy application code
# The main app.py file contains the Marimo application entry point
COPY --chown=user:user app.py .

# Switch to non-root user
# This is a security best practice to limit the potential damage if the container is compromised
#USER user

# Add healthcheck
# This allows Docker to monitor the health of the container
# Parameters:
# - interval=30s: Check every 30 seconds
# - timeout=30s: Allow 30 seconds for the check to complete
# - start-period=5s: Give 5 seconds grace period on startup
# - retries=3: Fail after 3 consecutive failed checks
#HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
#    CMD curl -f http://localhost:7860/ || exit 1

# Expose port
# This documents that the container listens on port 7860
# Note: This doesn't actually publish the port - that's done at runtime with -p flag
# EXPOSE 7860

FROM base AS prod

USER user

# Expose port
# This documents that the container listens on port 7860
# Note: This doesn't actually publish the port - that's done at runtime with -p flag
EXPOSE 7860

# Use exec form of ENTRYPOINT with CMD for proper signal handling
# The exec form is preferred as it doesn't start a shell, allowing signals to be passed correctly
ENTRYPOINT ["marimo"]
# The CMD provides default arguments to the ENTRYPOINT:
# - run: Runs the Marimo application
# - app.py: The main application file
# - --host 0.0.0.0: Binds to all network interfaces (required for container access)
# - --port 7860: The port the application listens on
CMD ["run", "app.py", "--host", "0.0.0.0", "--port", "7860"]

FROM base AS test

# Copy tests
COPY --chown=user:user tests /app/tests

RUN uv pip install --no-cache-dir -r /app/tests/requirements.txt && \
    ls -all

USER user

ENTRYPOINT ["pytest"]
