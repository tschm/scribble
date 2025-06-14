# Makefile for the scribble project
# This file contains commands for setting up the environment, formatting code,
# running tests, and other maintenance tasks.

.DEFAULT_GOAL := help

# Use system Python with uv
UV_SYSTEM_PYTHON := 1

uv:
	@curl -LsSf https://astral.sh/uv/install.sh | sh

# Format and lint the code using pre-commit
.PHONY: fmt
fmt: uv ## Run autoformatting and linting
	@uvx pre-commit run --all-files

# Clean up generated files
.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f

# Run the test suite using pytest with coverage
.PHONY: test
test: uv ## Run tests with coverage
	echo "# Installing dependencies..."
	grep -A 10 "# dependencies = \[" app.py | grep -E "^#\s+\".*\"" | cut -d'"' -f2 | xargs -I{} uv pip install {}
	uv pip install --no-cache-dir pytest
	uv run pytest -vv tests

# Display help information about available make targets
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

# Install and run Marimo for interactive notebooks
.PHONY: marimo
marimo: uv ## Install Marimo
	# will install dependencies straight out of app.py
	@uvx marimo edit apps/app.py --sandbox
