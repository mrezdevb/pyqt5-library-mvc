# 📚 Library Manager --- Release v2.7.0

## 🚀 What's New in This Release

### 🆕 Type Hints Everywhere

-   Full adoption of **PEP 484** type hints across controllers,
    services, repositories, and models.\
-   Stronger static analysis with **mypy**, ensuring safer refactors and
    fewer runtime surprises.\
-   Improved IDE autocompletion and developer experience.

### ⚙️ Config Manager (since v2.6.0)

-   Centralized settings with **pydantic-settings**.\
-   Runtime validation + computed `db_url`.\
-   Drop-in replacement for `os.getenv`.

### 🔄 Unit of Work (since v2.5.0)

-   Transaction boundary for all repositories.\
-   Guarantees atomic operations per request/command.

------------------------------------------------------------------------

## 🏗 Project Structure (unchanged)

``` text
app/
├── config/               # Settings (pydantic-settings)
├── controllers/          # Handles user interaction
├── db/                   # Engine, SessionLocal, Unit of Work
├── models/               # ORM models
├── observability/        # Logging & tracing
├── repositories/         # Data access
├── services/             # Business logic
├── ui/                   # Application UI
└── views/                # PyQt views
```

------------------------------------------------------------------------

## 🛠 Example with Type Hints

``` python
# app/services/book_service.py
from app.db.unit_of_work import UnitOfWork
from app.models.book import Book

class BookService:
	def __init__(self, uow: UnitOfWork) -> None:
		self.uow: UnitOfWork = uow
		self.book_repo: BookRepository = uow.book_repo
```

------------------------------------------------------------------------

## 📦 Installation & Usage

``` bash
pip install .
setup-env
library-install
library-run
library-uninstall
```

------------------------------------------------------------------------

## ⚠️ Migration Notes

-   Add **mypy** to your toolchain for static checks.\
-   Ensure all custom code follows **PEP 484** typing.\
-   No changes required for Config Manager or Unit of Work.

------------------------------------------------------------------------

## 🏷 Version Tag

**Tag:** `v2.7.0`
