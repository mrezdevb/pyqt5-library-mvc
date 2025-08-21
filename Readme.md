
# 📚 Library Manager — Release v2.5.0

## 🚀 What's New in This Release

### 🏗 Professional Project Structure
The project has been reorganized into a **scalable and maintainable architecture**:

```
app/
├── controllers/       # Handles UI events and user interaction
│   └── library_controller.py
├── db/                # Database initialization and session management
│   ├── db.py
│   ├── init_db.py
│   └── unit_of_work.py   # NEW: Unit of Work implementation
├── models/            # SQLAlchemy ORM models
│   ├── base.py
│   ├── book.py
│   ├── loan.py
│   └── member.py
├── observability/     # Logging, trace IDs, and helpers
│   ├── log_context.py
│   ├── logger_helpers.py
│   ├── logger.py
│   └── trace_decorators.py
├── repositories/      # Repository layer for clean database access
│   ├── book_repository.py
│   ├── loan_repository.py
│   └── member_repository.py
├── services/          # Business logic and rules
│   ├── book_service.py
│   ├── loan_service.py
│   └── member_service.py
├── ui/                # PyQt5 UI actions and widgets
│   ├── add_book.py
│   ├── add_member.py
│   ├── loan_book.py
│   ├── main.py
│   ├── remove_book.py
│   ├── remove_member.py
│   ├── return_book.py
│   ├── show_books.py
│   └── show_members.py
└── views/             # PyQt5 window layouts and forms
    ├── add_book_view.py
    ├── add_member_view.py
    ├── loan_book_view.py
    ├── main_window.py
    ├── remove_book_view.py
    ├── remove_member_view.py
    ├── return_book_view.py
    ├── show_books_view.py
    └── show_members_view.py

assets/               # Images and static assets
scripts/              # CLI entry points for install, uninstall, setup-env
tests/                # Unit and integration tests
requirements.txt      # Dependencies
setup.py              # Package configuration
```

---

### 🕵️‍♂️ Advanced Observability
- **Trace ID System**
  - Each action is tagged with a **unique Trace ID** for debugging and monitoring.
  - Works across all CRUD operations.
- **JSON Log Export**
  - Logs can be exported in **JSON format** for auditing and analytics.

### 🗄 Repository Pattern
- Clean **separation of concerns** for database access.
- Dedicated repositories:
  - `BookRepository`
  - `MemberRepository`
  - `LoanRepository`

### 🔄 Unit of Work (NEW in v2.5.0)
- Introduced **Unit of Work (UoW)** in `app/db/unit_of_work.py`.
- Provides **atomic transactions**:  
  - Multiple operations can be grouped and executed as a single unit.  
  - Ensures **consistency** in database changes.  
- Benefits:
  - Prevents partial commits.  
  - Increases testability and maintainability.  

### 🛠 CLI Commands
| Command                       | Description |
|-------------------------------|-------------|
| `library-install`             | Creates and initializes the database |
| `library-run`                 | Launches the Library Manager application |
| `library-uninstall`           | Drops the database |
| `setup-env`                   | Generates the `.env` configuration file |
| `pip uninstall library_manager` | Removes the package |

---

## 📦 Installation & Usage

### 1️⃣ Install the application
```bash
pip install .
```

### 2️⃣ Create the database
```bash
library-install
```

### 3️⃣ Run the application
```bash
library-run
```

### 4️⃣ Remove the database
```bash
library-uninstall
```

---

## ⚠️ Migration Notes
- Old logs may require conversion to JSON format to use the new export feature.  
- All service–database interactions **must now use the Repository + Unit of Work** pattern.  

```python
with UnitOfWork() as uow:
    book = uow.book_repository.get_by_id(book_id)
    ...
    uow.commit()
```


---

## 🏷 Version Tag
**Tag:** `v2.5.0`

