# 📚 Library Manager — Release v2.6.0

## 🚀 What's New in This Release

### 🆕 Config Manager (NEW in v2.6.0)
A centralized configuration system powered by **pydantic-settings**:
- Single source of truth at `app/config/settings.py`
- Reads from `.env` (created via `setup-env`) with runtime validation
- Provides a computed `db_url` for SQLAlchemy
- Strong typing for safer refactors
- Easy access anywhere: `from app.config.settings import settings`

### ✨ Service & Repository Ergonomics
- Services now read configuration from the Config Manager (e.g., `settings.max_borrow_limit`).
- Clearer logs and error messages across services.
- Minor repository query cleanups for readability.

### 🔄 Unit of Work (introduced in v2.5.0 — still here)
Unit of Work was **added in v2.5.0** and remains the backbone of consistent transactions. The pattern ensures atomic operations across repositories in each request/command.

---

## 🏗 Project Structure (updated)
```
app/
├── config/
│   └── settings.py         # NEW: Config Manager (pydantic-settings)
├── controllers/
│   └── library_controller.py
├── db/
│   ├── db.py               # SQLAlchemy engine & SessionLocal
│   ├── init_db.py          # DB bootstrap (imports models & creates tables)
│   └── unit_of_work.py     # Unit of Work (since v2.5.0)
├── models/
│   ├── base.py
│   ├── book.py
│   ├── loan.py
│   └── member.py
├── observability/
│   ├── log_context.py
│   ├── logger_helpers.py
│   ├── logger.py
│   └── trace_decorators.py
├── repositories/
│   ├── book_repository.py
│   ├── loan_repository.py
│   └── member_repository.py
├── services/
│   ├── book_service.py
│   ├── loan_service.py
│   └── member_service.py
├── ui/
│   ├── add_book.py
│   ├── add_member.py
│   ├── loan_book.py
│   ├── main.py
│   ├── remove_book.py
│   ├── remove_member.py
│   ├── return_book.py
│   ├── show_books.py
│   └── show_members.py
└── views/
    ├── add_book_view.py
    ├── add_member_view.py
    ├── loan_book_view.py
    ├── main_window.py
    ├── remove_book_view.py
    ├── remove_member_view.py
    ├── return_book_view.py
    ├── show_books_view.py
    └── show_members_view.py

assets/
scripts/                  # CLI: install/uninstall/setup-env
tests/
requirements.txt
setup.py
```

---

## ⚙️ Config Manager

### Location
`app/config/settings.py`

### Example
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    log_level: str = "DEBUG"
    max_borrow_limit: int

    @property
    def db_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}/{self.db_name}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
```

### How to use
```python
from app.config.settings import settings

engine = create_engine(settings.db_url, echo=False, future=True)
limit = settings.max_borrow_limit
```

### `.env` template
```
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=library_db
DB_HOST=localhost
LOG_LEVEL=DEBUG
MAX_BORROW_LIMIT=3
```

### CLI helpers
- `setup-env` — generates `.env` interactively.
- `library-install` — creates the database and initializes tables.
- `library-run` — launches the application.
- `library-uninstall` — drops the database.

> Note: If you previously used `os.getenv`, migrate to `from app.config.settings import settings`.

---

## 🧠 Unit of Work (since v2.5.0)

**Where**: `app/db/unit_of_work.py`  
**Why**: atomic transactions across repositories.

```python
from app.db.unit_of_work import UnitOfWork

with UnitOfWork() as uow:
    book = uow.book_repo.query_by_isbn("978...").first()
    # mutate entities / add or remove records
    # no need to call commit explicitly; __exit__ handles commit/rollback
```

---

## 🛠 Code Snippets

### Engine & Session
```python
# app/db/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings

engine = create_engine(settings.db_url, echo=False, future=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=True,
    bind=engine,
    expire_on_commit=False,
)
```

### LoanService (using Config Manager)
```python
# app/services/loan_service.py
from app.config.settings import settings

max_borrow_limit = settings.max_borrow_limit
```

---

## 📦 Installation & Usage

1. **Install the application**
   ```bash
   pip install .
   ```

2. **Create the `.env` file (interactive)**
   ```bash
   setup-env
   ```

3. **Create the database**
   ```bash
   library-install
   ```

4. **Run the application**
   ```bash
   library-run
   ```

5. **Remove the database**
   ```bash
   library-uninstall
   ```

---

## ⚠️ Migration Notes
- If you have custom environment variables, align them with the **Config Manager** fields or override via `.env`.
- Replace direct `os.getenv` calls with `from app.config.settings import settings` for consistency and validation.
- Unit of Work has been available since **v2.5.0**; no changes needed to keep using it.

---

## 🏷 Version Tag
**Tag:** `v2.6.0`
