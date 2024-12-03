.DEFAULT_GOAL := help

.PHONY: install
install:  ## Install a virtual environment
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv sync -vv
	@echo 'Please perform'
	@echo 'source .venv/bin/activate'

.PHONY: fmt
fmt:  ## Run autoformatting and linting
	@uv pip install pre-commit
	@uv run pre-commit install
	@uv run pre-commit run --all-files

.PHONY: test
test: install ## Run tests
	@uv run pytest
