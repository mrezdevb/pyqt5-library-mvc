# 📦 Release v1.9.0

## 🚀 New Features
- **Book Status Column in Show Books**  
  - Added a new **Status** column in the *Show Books* table to indicate whether each book is currently borrowed or available.
- **Borrowed Books Column in Show Members**  
  - Added a **Borrowed Books** column in the *Show Members* table to display the titles of books each member has currently borrowed.

## 🖥 UI Improvements
- Updated **Show Books** and **Show Members** tables to include the new columns while keeping them read-only.
- Improved table resizing and formatting for better readability.

## ⚙ Backend & Logic Enhancements
- Extended `show_books` logic to return book availability status.
- Extended `show_members` logic to retrieve and display a list of borrowed books per member.
- Optimized database queries with `joinedload` to reduce SQL calls.

### Install the application:
```bash
pip install .
```

### Create the database:
```bash
library-install
```

### Run the application:
```bash
library-run
```

### Remove the database:
```bash
library-uninstall
```

### Uninstall the application:
```bash
pip uninstall library_manager
```
---
**Tag:** `v1.9.0`
