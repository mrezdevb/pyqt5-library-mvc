# 📚 Library Management System (v1.2.0)

A modular, GUI-based library management system built with **Python**, **PyQt5**, **PostgreSQL**, and **SQLAlchemy**. This project implements the MVC (Model-View-Controller) pattern for clean architecture, modularity, and maintainability.

---

## 🧩 Features

- Add, remove, loan, and return books
- Add and remove members
- View books and members list
- GUI built using PyQt5 (.ui converted to `.py`)
- Database connectivity via PostgreSQL and SQLAlchemy ORM
- Modular architecture: models, views, controllers, and utilities
- Testable structure with `pytest`
- Automatic `.env` creation script for easier setup

---

## 🗂️ Project Structure

```
library_app/
├── controllers/
├── models/
├── views/
├── ui/
├── utils/
├── test/
├── db.py
├── init_db.py
├── main.py
├── install.py
├── setup_env.py   # Script to automatically create `.env` file
├── images/
│   └── main_window.png
├── __init__.py
setup.py
requirements.txt
README.md
```

---

## 🚀 Installation

Make sure you have **Python 3.8+** and **PostgreSQL** installed and configured on your system.

1. Clone the repository:

```bash
git clone https://github.com/mrezdevb/pyqt5-library-mvc.git
```

2. Install the package along with dependencies:

```bash
pip install .
```

> ℹ️ All dependencies defined in `requirements.txt` will be automatically installed through `setup.py`.

3. Run the application:

```bash
library-app
```

---

## 🧪 Running Tests

The project uses `pytest` for unit testing. To run all tests:

```bash
pytest library_app/test
```

---

## 🔮 Roadmap / Future Plans

- Improve search and filtering options.
- Enhance UI/UX with better design and responsiveness.
- Add role-based authentication.

---
## 📃 License

MIT License

---

## 📞 Contact / Author

Mohammadreza Mahdian  
Email: mrez.devb@gmail.com  
GitHub: https://github.com/mrezdevb
