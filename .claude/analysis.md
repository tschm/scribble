# Scribble Repository Analysis

Generated: 2026-01-17

## Project Overview

**Scribble** is a creative tool for generating artistic text effects using mathematical transformations. Originally created to design wedding name plates, it transforms text into visually stunning designs by applying complex mathematical functions to letter shapes represented as points in the complex plane.

| Attribute | Value |
|-----------|-------|
| Name | scribble |
| Version | 0.0.0 (dynamic versioning) |
| Python | >=3.12 |
| License | MIT |
| Author | Thomas Schmelzer |
| Build System | uv (modern Python package manager) |

---

## Architecture

### Core Algorithm

The application transforms text through a mathematical pipeline:

1. **Letter Encoding**: Each uppercase letter (A-Z) is mapped to an array of complex numbers defining its shape as coordinate points
2. **Segment Discretization**: Adjacent points are connected by straight segments, each discretized into 100 auxiliary points
3. **Mathematical Transformation**: A complex function is applied to all points (e.g., `sinh(3*z)`, `tanh((-1+2j)*z)`, `exp((-1+2j)*z)`)
4. **Visualization**: Transformed points are plotted using Plotly to create the artistic effect

### Directory Structure

```
scribble/
├── apps/
│   └── app.py              # Main Marimo application (331 lines)
├── book/
│   ├── marimo/             # Documentation notebooks
│   │   └── rhiza.py
│   ├── pdoc-templates/     # Custom pdoc templates
│   └── minibook-templates/ # Custom minibook templates
├── tests/
│   ├── test_letter.py      # Letter function tests
│   ├── test_plot.py        # Plot creation tests
│   ├── test_series.py      # Series generation tests
│   ├── test_input_event.py # Input event tests
│   ├── test_output_cell.py # Output cell tests
│   └── test_rhiza/         # Rhiza framework tests (11 modules)
├── .rhiza/                 # Rhiza framework configuration
│   ├── .env                # Environment variables
│   ├── .cfg.toml           # Bumpversion configuration
│   ├── requirements/       # Dev requirements (tests, marimo, docs, tools)
│   ├── scripts/            # Automation scripts (5 scripts)
│   └── customisations/     # Custom build scripts
├── .github/
│   └── workflows/          # 11 GitHub Actions workflows
├── Makefile                # Main entry point (includes modular makefiles)
├── pyproject.toml          # Project metadata and dependencies
├── ruff.toml               # Linting configuration
├── pytest.ini              # Test configuration
└── .pre-commit-config.yaml # Pre-commit hooks
```

### Key Application Components

**`apps/app.py`** - Main Marimo application containing:

| Function | Purpose |
|----------|---------|
| `letter(x: str)` | Maps uppercase letters to complex number coordinate arrays |
| `function_map()` | Dictionary of available mathematical transformation functions |
| `series(string, n, fct)` | Generates transformed point series for text strings |
| `create(name, fct, event, n)` | Creates the final Plotly visualization figure |

**Marimo UI Components**:
- Name input field
- Function dropdown selector (tanh, sinh, exp variants)
- Event description input
- Interactive Plotly output with download capability

---

## Dependencies

### Production Dependencies

None (empty `dependencies` array in pyproject.toml)

### Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| marimo | >=0.18.0 | Interactive notebook/web interface |
| numpy | >=2.4.0 | Numerical computing, complex number operations |
| plotly | >=6.5.0 | Interactive visualization |
| pandas | >=2.3.3 | Data manipulation |

### Additional Requirements (`.rhiza/requirements/`)

| File | Packages |
|------|----------|
| tests.txt | pytest, pytest-cov, pytest-html, pytest-mock |
| marimo.txt | marimo>=0.18.0 |
| docs.txt | pdoc>=16.0.0 |
| tools.txt | pre-commit, python-dotenv, typer |

---

## Test Suite

### Test Structure

**Application Tests** (`tests/`):
- `test_letter.py` - Letter encoding function validation
- `test_plot.py` - Plot creation and figure structure
- `test_series.py` - Series generation with transformations
- `test_input_event.py` - UI input handling
- `test_output_cell.py` - Output cell rendering

**Framework Tests** (`tests/test_rhiza/`):
- `test_structure.py` - Project structure validation
- `test_makefile.py` - Makefile target testing
- `test_makefile_gh.py` - GitHub-specific targets
- `test_docstrings.py` - Documentation validation
- `test_coverage_badge.py` - Badge generation
- `test_notebooks.py` - Marimo notebook execution
- `test_readme.py` - README consistency
- `test_release_script.py` - Release workflow
- `test_marimushka_script.py` - Notebook export
- `test_updatereadme_script.py` - README automation
- `test_requirements_folder.py` - Requirements validation
- `test_git_repo_fixture.py` - Git fixture tests

### Test Configuration (`pytest.ini`)

```ini
log_cli = true
log_cli_level = DEBUG
addopts = -ra
```

### Coverage Output

- HTML reports: `_tests/html-coverage/`
- JSON data: `_tests/coverage.json`
- Test reports: `_tests/html-report/report.html`

---

## CI/CD Workflows

### GitHub Actions (`.github/workflows/`)

| Workflow | File | Trigger | Purpose |
|----------|------|---------|---------|
| CI | rhiza_ci.yml | push/PR to main | Run tests on Python version matrix |
| Pre-commit | rhiza_pre-commit.yml | push/PR to main | Ruff linting and formatting |
| Deptry | rhiza_deptry.yml | push/PR | Check missing/obsolete dependencies |
| Marimo | rhiza_marimo.yml | push/PR | Execute all Marimo notebooks |
| CodeQL | rhiza_codeql.yml | push/PR/schedule | Security scanning |
| Docker | rhiza_docker.yml | push/PR | Dockerfile linting and build validation |
| Release | rhiza_release.yml | tag push | Multi-phase release pipeline |
| Sync | rhiza_sync.yml | manual/schedule | Sync with Rhiza template |
| Validate | rhiza_validate.yml | push/PR | Validate project structure |
| Book | rhiza_book.yml | push/PR | Generate documentation |
| Devcontainer | rhiza_devcontainer.yml | push/PR | Build devcontainer image |

### Dependency Automation

**Renovate** (`renovate.json`):
- Enabled managers: pep621, pre-commit, github-actions, devcontainer, dockerfile
- Auto-merge: minor versions
- Schedule: Tuesdays before 10am
- Semantic commits enabled

---

## Code Quality

### Ruff Configuration (`ruff.toml`)

| Setting | Value |
|---------|-------|
| Line length | 120 |
| Target Python | 3.11+ |
| Quote style | Double quotes |
| Indent style | Spaces |

**Enabled Lint Rules**:
- D: pydocstyle (Google convention)
- E: pycodestyle errors (PEP 8)
- F: pyflakes (logical errors)
- I: isort (import sorting)
- N: pep8-naming (PEP 8 naming)
- W: pycodestyle warnings
- UP: pyupgrade (syntax modernization)

**Per-File Exceptions**:
- `tests/**/*.py`: Allow assert statements (S101)
- `book/marimo/*.py`: Allow non-lowercase names (N803), asserts (S101)

### Pre-commit Hooks (`.pre-commit-config.yaml`)

| Hook | Repository | Version | Purpose |
|------|------------|---------|---------|
| check-toml | pre-commit/pre-commit-hooks | v6.0.0 | Validate TOML |
| check-yaml | pre-commit/pre-commit-hooks | v6.0.0 | Validate YAML |
| ruff | astral-sh/ruff-pre-commit | v0.14.11 | Linting with auto-fix |
| ruff-format | astral-sh/ruff-pre-commit | v0.14.11 | Code formatting |
| markdownlint | igorshubovych/markdownlint-cli | v0.47.0 | Markdown linting |
| check-renovate | python-jsonschema/check-jsonschema | 0.36.0 | Validate renovate.json |
| check-github-workflows | python-jsonschema/check-jsonschema | 0.36.0 | Validate workflows |
| actionlint | rhysd/actionlint | v1.7.10 | GitHub Actions validation |
| validate-pyproject | abravalheri/validate-pyproject | v0.24.1 | Validate pyproject.toml |
| update-readme-help | local | - | Auto-update README |

---

## Makefile Targets

### Bootstrap

| Target | Description |
|--------|-------------|
| `install-uv` | Ensure uv/uvx is installed |
| `install` | Create .venv and install all dependencies |
| `clean` | Remove artifacts and prune git branches |

### Development

| Target | Description |
|--------|-------------|
| `marimo` | Start Marimo development server |
| `test` | Run pytest with coverage reports |
| `benchmark` | Run performance benchmarks |
| `fmt` | Run pre-commit hooks (ruff format + lint) |
| `deptry` | Check for dependency issues |

### Documentation

| Target | Description |
|--------|-------------|
| `docs` | Generate pdoc documentation |
| `marimushka` | Export Marimo notebooks to HTML |
| `book` | Build complete documentation book |

### Release

| Target | Description |
|--------|-------------|
| `bump` | Bump version using bumpversion |
| `release` | Create tag and push with prompts |
| `validate` | Validate against Rhiza template |
| `sync` | Sync with Rhiza template repository |

---

## Rhiza Framework

The project uses the **Rhiza framework** (from `jebel-quant/rhiza`) for standardized Python project management.

### Environment Variables (`.rhiza/.env`)

```bash
MARIMO_FOLDER=book/marimo
SOURCE_FOLDER=src
SCRIPTS_FOLDER=.rhiza/scripts
CUSTOM_SCRIPTS_FOLDER=.rhiza/customisations/scripts
BOOK_TITLE=Project Documentation
BOOK_SUBTITLE=Generated by minibook
PDOC_TEMPLATE_DIR=book/pdoc-templates
DOCFORMAT=google
DEFAULT_AI_MODEL=gpt-4.1
```

### Automation Scripts (`.rhiza/scripts/`)

| Script | Purpose |
|--------|---------|
| book.sh | Book generation automation |
| generate-coverage-badge.sh | Coverage badge creation |
| marimushka.sh | Marimo notebook export |
| release.sh | Release workflow orchestration |
| update-readme-help.sh | README Makefile help auto-update |

---

## Editor Configuration

### EditorConfig (`.editorconfig`)

| File Type | Indentation | Line Ending |
|-----------|-------------|-------------|
| All files | - | LF |
| Python/RST/Text | 4 spaces | LF |
| YAML/JSON | 2 spaces | LF |

### Git Ignore Patterns

- Python artifacts: `__pycache__/`, `*.py[cod]`, `*.egg-info/`
- Virtual environments: `.venv`, `.idea`, `.ruff_cache`
- Test outputs: `_tests`, `.pytest_cache`, `htmlcov/`
- Build artifacts: `build/`, `dist/`
- Marimo cache: `__marimo__`

---

## File Statistics

| Category | Count |
|----------|-------|
| Python source files | 2 (apps/, book/marimo/) |
| Test files | 17 |
| GitHub workflows | 11 |
| Makefile includes | 6 |
| Pre-commit hooks | 9 |
| Rhiza scripts | 5 |

---

## Notes

1. **SOURCE_FOLDER Mismatch**: The `.rhiza/.env` sets `SOURCE_FOLDER=src` but the main application is in `apps/`. This may affect deptry checks.

2. **No Docker Configuration**: The `docker/` directory does not exist. The Docker workflow gracefully skips when no Dockerfile is present.

3. **Dynamic Versioning**: Version is set to `0.0.0` and managed via bumpversion in `.rhiza/.cfg.toml`.

4. **Marimo Notebook Format**: The main app uses Marimo's `@app.function` and `@app.cell` decorators for reactive notebook functionality.

---

## Quality Assessment

### Overall Score: 8.0 / 10

### Category Breakdown

#### 1. Code Quality (7.8/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Code Organization | 7 | Single app file with clear structure; apps/ vs src/ naming inconsistency |
| Docstrings | 9 | Comprehensive Google-style docstrings on all functions |
| Type Hints | 6 | Partial coverage; `letter()` and `series()` have hints, some internal functions lack them |
| Code Style Consistency | 9 | Ruff enforced via pre-commit; consistent formatting throughout |

**Strengths**: Well-documented functions with clear purpose descriptions. Consistent style enforcement.
**Areas for Improvement**: Add type hints to all functions; resolve apps/ vs src/ folder naming.

---

#### 2. Testing (7.3/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Test Coverage | 7 | Core functions tested; coverage reports generated |
| Test Organization | 8 | Logical separation by function; parametrized tests used |
| Test Quality | 7 | Edge cases covered (empty name, space character, invalid input) |
| Test Documentation | 7 | All tests have docstrings explaining purpose |

**Strengths**: Good use of pytest parametrization for multiple scenarios. Edge case testing present.
**Areas for Improvement**: Add integration tests for full workflow; increase coverage metrics visibility.

---

#### 3. CI/CD (9.0/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Pipeline Completeness | 9 | 11 workflows covering test, lint, security, docs, release |
| Automation Level | 9 | Renovate auto-merge, dynamic Python version matrix |
| Security Scanning | 9 | CodeQL for Python and Actions; scheduled scans |
| Release Process | 9 | Multi-phase release workflow with PyPI publishing |

**Strengths**: Comprehensive automation; dynamic version matrix; excellent security posture.
**Areas for Improvement**: Consider adding performance regression tests in CI.

---

#### 4. Documentation (7.0/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| README Quality | 8 | Clear purpose, installation, usage, and algorithm explanation |
| API Documentation | 5 | Docstrings present but no generated API docs published |
| Contributing Guide | 8 | Clear checklist, code style, and testing instructions |
| In-Code Comments | 7 | Algorithm steps documented; letter data source cited |

**Strengths**: README explains the mathematical concept well. Contributing guide is actionable.
**Areas for Improvement**: Generate and publish API documentation; add architecture diagrams.

---

#### 5. Dependency Management (8.3/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Version Pinning | 8 | uv.lock for reproducibility; minimum versions in pyproject.toml |
| Dependency Freshness | 9 | Renovate enabled with scheduled updates |
| Security Updates | 8 | Automated PRs for dependency updates |
| Dependency Hygiene | 8 | deptry checks for unused/missing deps |

**Strengths**: Modern tooling with uv; automated dependency management.
**Areas for Improvement**: Consider stricter version upper bounds for stability.

---

#### 6. Project Structure (8.0/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Directory Organization | 7 | Clear separation but SOURCE_FOLDER mismatch (src vs apps) |
| Configuration Files | 9 | Well-organized; modular Makefiles |
| Separation of Concerns | 8 | Tests, docs, app code clearly separated |
| Naming Conventions | 8 | Consistent file naming; rhiza_ prefix for workflows |

**Strengths**: Modular Makefile includes; clear test structure.
**Areas for Improvement**: Fix SOURCE_FOLDER environment variable to match actual app location.

---

#### 7. Developer Experience (9.0/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Setup Ease | 9 | Single `make install` sets up everything |
| Makefile Usability | 9 | Comprehensive targets with colorized help |
| Editor Configuration | 9 | EditorConfig present; IDE-agnostic settings |
| Local Development | 9 | `make marimo` provides instant interactive development |

**Strengths**: Excellent onboarding experience; well-documented Makefile.
**Areas for Improvement**: Add devcontainer configuration for consistent environments.

---

#### 8. Security (8.3/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Static Analysis | 9 | CodeQL scanning on push/PR and weekly schedule |
| Dependency Scanning | 8 | Renovate security updates; deptry checks |
| Secrets Management | 8 | .gitignore excludes .env files; no hardcoded secrets |
| Permissions | 8 | Minimal workflow permissions (contents: read) |

**Strengths**: Comprehensive security scanning; proper gitignore patterns.
**Areas for Improvement**: Consider adding SAST tool beyond CodeQL; document security policy.

---

#### 9. Maintainability (8.3/10)

| Subcategory | Score | Notes |
|-------------|-------|-------|
| Code Simplicity | 9 | Single-purpose functions; clear algorithm flow |
| Technical Debt | 8 | Clean codebase; few workarounds or hacks |
| Framework Adoption | 8 | Rhiza provides standardization and consistency |
| Scalability | 8 | Modular design allows easy extension |

**Strengths**: Simple, focused codebase; Rhiza framework reduces maintenance burden.
**Areas for Improvement**: Extract letter definitions to data file for easier modification.

---

### Summary by Category

| Category | Score |
|----------|-------|
| Code Quality | 7.8 |
| Testing | 7.3 |
| CI/CD | 9.0 |
| Documentation | 7.0 |
| Dependency Management | 8.3 |
| Project Structure | 8.0 |
| Developer Experience | 9.0 |
| Security | 8.3 |
| Maintainability | 8.3 |
| **Overall** | **8.0** |

---

### Top Recommendations

1. **Fix SOURCE_FOLDER mismatch**: Update `.rhiza/.env` to set `SOURCE_FOLDER=apps` or move app to `src/`
2. **Add type hints**: Complete type annotations for all functions to improve IDE support
3. **Generate API docs**: Use pdoc to publish documentation from existing docstrings
4. **Extract letter data**: Move letter coordinate definitions to a separate data file (JSON/YAML)
5. **Add devcontainer**: Create `.devcontainer/` configuration for reproducible development environments
