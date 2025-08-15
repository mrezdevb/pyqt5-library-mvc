# 📚 Library Management System (v1.5.0)

A modular, GUI-based library management system built with **Python**, **PyQt5**, **PostgreSQL**, and **SQLAlchemy**, following the **MVC** pattern for clean architecture and maintainability.

---

## 🆕 What's New in v1.5.0

- **Added limit on the number of books each member can borrow.**  
- **Maximum borrow limit configurable via `MAX_BORROW_LIMIT` in `.env`.**  

---

## 🧩 Main Features

- Add, remove, loan, and return books
- Add and remove members
- Search books by title, author, or ISBN
- View books and members list
- GUI built with PyQt5
- Database via PostgreSQL & SQLAlchemy ORM
- Modular architecture (models, views, controllers)
- Fully testable with `pytest`

---

## ⚙️ Configuration

Set maximum borrow limit in `.env`:

```
MAX_BORROW_LIMIT=3
```

---

## 🚀 Installation & Commands

Make sure you have **Python 3.8+** and **PostgreSQL** installed and configured.

1. Clone the repository:

```bash
git clone https://github.com/mrezdevb/pyqt5-library-mvc.git
```

2. Install the package with dependencies.
   **During installation, the system will automatically create a `.env` file** (no manual setup needed) and initialize the database:

```bash
pip install .
library-install
```

3. Run the application:

```bash
library-run
```

4. Uninstall the database:

```bash
library-uninstall
```

5. Uninstall the package:

```bash
pip uninstall library_manager
```

---
