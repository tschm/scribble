# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Scribble is a creative tool for generating artistic text effects using mathematical transformations. It transforms text into visual designs by applying complex functions (tanh, sinh, exp) to letter shapes represented as points in the complex plane. Built with Marimo for interactive web visualization.

## Development Commands

```bash
make install    # Create .venv and install dependencies via uv
make test       # Run pytest with coverage (reports in _tests/)
make fmt        # Run pre-commit hooks (ruff format + lint)
make marimo     # Start Marimo development server
make deptry     # Check for unused/missing dependencies
make benchmark  # Run performance benchmarks
```

### Running a Single Test

```bash
.venv/bin/python -m pytest tests/test_file.py::test_function -v
```

## Architecture

**Core Application**: `apps/app.py` - Single Marimo app containing:
- Letter definitions as complex number sequences (A-Z mapped to coordinate arrays)
- Mathematical transformation functions (tanh, sinh, exp variations)
- `series()` function that discretizes letter segments and applies transformations
- Plotly-based visualization with subplots

**Key Algorithm Flow**:
1. Each letter → array of complex points defining its shape
2. Adjacent points connected by segments, each discretized to 100 points
3. Complex function applied to all points (e.g., `sinh(3*z)`)
4. Transformed points plotted to create artistic effect

**Project Structure**:
- `apps/` - Main Marimo application
- `book/marimo/` - Documentation notebooks
- `tests/` - pytest test suite
- `.rhiza/` - Build framework configuration (from jebel-quant/rhiza template)

## Code Style

- **Linter**: Ruff with 120 char line length, Python 3.11+ target
- **Docstrings**: Google style convention
- **Rules enforced**: pydocstyle (D), pycodestyle (E/W), pyflakes (F), isort (I), pep8-naming (N), pyupgrade (UP)
- Tests allow `assert` statements (S101 ignored)
- Marimo files allow non-lowercase variable names (N803 ignored)

## Dependencies

Managed via `uv` with `pyproject.toml` and `uv.lock`. Key dependencies:
- marimo (interactive notebooks)
- numpy (numerical operations)
- plotly (visualization)
- kaleido (image export)

Add dependencies with: `uv add <package>`
