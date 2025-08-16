# 📦 Release v1.7.0

## 🚀 New Features
- **Advanced Book Filtering in UI**  
  - Added a filter option in the **Show Books** view allowing users to switch between:
    - **All Books** – Displays all registered books.
    - **Available Books** – Displays only books that are not currently borrowed.
- **Smart Search Messages**  
  - Search messages are now more informative and context-aware:
    - If no book is found → *"No books found for `<keyword>`."*
    - If books exist but are all borrowed → *"Books matching `<keyword>` are currently borrowed."*
  - This helps users know when a book exists but is temporarily unavailable.

## 🖥 UI Improvements
- Updated **Show Books** view to integrate search and filtering seamlessly.
- Optimized table rendering for faster updates when changing filters or performing searches.
- Ensured table cells remain read-only to prevent accidental edits.

## ⚙ Backend & Logic Enhancements
- Refactored `show_books` and `search_books` functions to support filtering and status-based messages.
- Optimized queries to reduce unnecessary executions and improve code maintainability.
- Enhanced logging for search and filter operations to assist in debugging and monitoring.

## 📋 Installation & Usage
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
**Tag:** `v1.7.0`  

