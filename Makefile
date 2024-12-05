.DEFAULT_GOAL := help

.PHONY: install
install:  ## Install a virtual environment
	@curl -LsSf https://astral.sh/uv/install.sh | sh
	@uv pip install -r requirements.txt
	@echo 'Please perform'
	@echo 'source .venv/bin/activate'

.PHONY: fmt
fmt:  ## Run autoformatting and linting
	@uv pip install pre-commit
	@uv run pre-commit install
	@uv run pre-commit run --all-files

.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f

.PHONY: test
test: install ## Run tests
	@uv pip install pytest
	@uv run pytest

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

.PHONY: deptry
deptry: install ## run deptry
	@uv pip install deptry
	@uv run deptry .

.PHONY: marimo
marimo: install ## Install Marimo
	@uv pip install marimo
	@uv run marimo edit app.py

.PHONY: app
app: install
	@uv pip install marimo
	@uv run marimo run app.py
