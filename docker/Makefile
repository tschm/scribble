
.DEFAULT_GOAL := help

# Clean up generated files and remove stale branches
.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f
	@git branch -v | grep "\[gone\]" | cut -f 3 -d ' ' | xargs git branch -D

# Display help information about available make targets
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort

# Build and run the Docker container for the application
.PHONY: build
build: ## Build and run Docker container
	@docker build -f Dockerfile -t marimo-app ..
	@docker run -it --rm -p 7860:7860 marimo-app

# Test the Docker container
.PHONY: test-docker
test-docker: ## Test Docker container build and functionality
	@chmod +x test_docker.sh
	@cd $(CURDIR) && ./test_docker.sh
