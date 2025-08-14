# 📚 Library Management System (v1.4.0)

A modular, GUI-based library management system built with **Python**, **PyQt5**, **PostgreSQL**, and **SQLAlchemy**.  
Implements the MVC (Model-View-Controller) pattern for clean architecture, modularity, and maintainability.

---

## 🆕 What's New in v1.4.0

- **Search feature** for finding books by **title**, **author**, or **ISBN**.
- **Database removal** command (`library-uninstall`).
- **Database creation** command (`library-install`) integrated with the installation process.
- Improved installation and execution flow using `console_scripts` commands.
- Various bug fixes and stability improvements.

---

## 🧩 Features

- Add, remove, loan, and return books
- Add and remove members
- **Search books by title/author/ISBN**
- View books and members list
- GUI built using PyQt5 (.ui converted to `.py`)
- Database connectivity via PostgreSQL and SQLAlchemy ORM
- Modular architecture: models, views, controllers, and utilities
- Testable structure with `pytest`

---

## 🗂️ Project Structure

```
├── library_app
│   ├── controllers
│   │   ├── __init__.py
│   │   └── library.py
│   ├── db.py
│   ├── images
│   │   └── main_window.png
│   ├── init_db.py
│   ├── __init__.py
│   ├── install.py
│   ├── main.py
│   ├── models
│   │   ├── base.py
│   │   ├── book.py
│   │   ├── __init__.py
│   │   ├── loan.py
│   │   └── member.py
│   ├── test
│   │   ├── __init__.py
│   │   ├── test_controllers
│   │   │   ├── __init__.py
│   │   │   └── test_library_management.py
│   │   ├── test_models
│   │   │   ├── __init__.py
│   │   │   ├── test_book.py
│   │   │   ├── test_loan.py
│   │   │   └── test_member.py
│   │   └── test_utils
│   │       ├── __init__.py
│   │       └── test_logger.py
│   ├── ui
│   │   ├── add_book.py
│   │   ├── add_member.py
│   │   ├── __init__.py
│   │   ├── loan_book.py
│   │   ├── main.py
│   │   ├── remove_book.py
│   │   ├── remove_member.py
│   │   ├── return_book.py
│   │   ├── show_books.py
│   │   └── show_members.py
│   ├── uninstall.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── logger.py
│   └── views
│       ├── add_book_view.py
│       ├── add_member_view.py
│       ├── __init__.py
│       ├── loan_book_view.py
│       ├── main_window.py
│       ├── remove_book_view.py
│       ├── remove_member_view.py
│       ├── return_book_view.py
│       ├── show_books_view.py
│       └── show_members_view.py
├── README.md
├── requirements.txt
└── setup.py
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

## 🧪 Running Tests

```bash
pytest library_app/test
```

---

## 🔮 Roadmap / Future Plans

- Add advanced filtering.
- Limit the number of books each member can borrow.
- Display the list of books borrowed by each member.
- Show book availability status in the books table.

---

## 📃 License

MIT License

---

## 📞 Contact

Mohammadreza Mahdian  
Email: mrez.devb@gmail.com  
GitHub: https://github.com/mrezdevb  
