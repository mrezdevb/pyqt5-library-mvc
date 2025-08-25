# 📚 Library Manager --- Release v2.9.0

## 🚀 What's New in This Release

### 🆕 Unified Linting Script
-   Added **`make-lint`** command to run all static analysis tools at once:
    -   **flake8** → style & linting
    -   **black** → auto-formatting
    -   **mypy** → static type checking
-   No need to run tools separately — one command handles all.

### 🔧 Minor Function Improvements
-   Small refactoring and performance improvements in service and repository methods.
-   More consistent return types thanks to type hints.

### 🆕 Static Analysis & Code Quality (since v2.8.0)
-   Integrated **flake8**, **black**, **mypy** across the project.
-   Ensures clean, consistent, and type-safe codebase.

### 🆕 Type Hints Everywhere (since v2.7.0)
-   Full adoption of **PEP 484** type hints across controllers,
    services, repositories, and models.
-   Improved IDE autocompletion and developer experience.

### ⚙️ Config Manager (since v2.6.0)
-   Centralized settings with **pydantic-settings**.  
-   Runtime validation + computed `db_url`.
-   Drop-in replacement for `os.getenv`.

### 🔄 Unit of Work (since v2.5.0)
-   Transaction boundary for all repositories.
-   Guarantees atomic operations per request/command.

------------------------------------------------------------------------

## 📦 Installation & Usage

```bash
pip install .
setup-env
library-install
library-run
library-uninstall
```

------------------------------------------------------------------------

## ✅ Static Analysis & Formatting

### 🚀 Run All (recommended)
```bash
make lint
```

### 🔍 Individual Tools
```bash
flake8 .
black .
mypy app/ scripts/
```

------------------------------------------------------------------------

## ⚠️ Migration Notes
-   Use `make lint` for unified static analysis instead of separate commands.  
-   Ensure all code passes checks before commits.  
-   Type hints remain **mandatory** for new contributions.  

------------------------------------------------------------------------

## 🏷 Version Tag
**Tag:** `v2.9.0`
