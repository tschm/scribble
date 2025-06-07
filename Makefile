# Makefile for the scribble project
# This file contains commands for setting up the environment, formatting code,
# running tests, and other maintenance tasks.

.DEFAULT_GOAL := help

# Use system Python with uv
UV_SYSTEM_PYTHON := 1

venv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv venv

# Mark install target as phony (not producing a file named 'install')
.PHONY: install
install: venv ## Install a virtual environment
	@uv pip install --upgrade pip
	@uv pip install --no-cache-dir -r requirements.txt


# Format and lint the code using pre-commit
.PHONY: fmt
fmt: venv ## Run autoformatting and linting
	@uvx pre-commit install
	@uvx pre-commit run --all-files

# Clean up generated files
.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f

# Run the test suite using pytest with coverage
.PHONY: test
test: install ## Run tests with coverage
	@uv pip install --no-cache-dir pytest pytest-cov
	@uv run pytest -vv tests

# Display help information about available make targets
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

# Install and run Marimo for interactive notebooks
.PHONY: marimo
marimo: install ## Install Marimo
	@uv run marimo edit app.py
