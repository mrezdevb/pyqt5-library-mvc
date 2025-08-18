# 📚 Library Manager — Release v2.0.0

## 🚀 What's New in This Release

### 🏗 Architecture Upgrade
- **Migrated to Service Layer Architecture**  
  The project structure now follows a clear **Service Layer** pattern, with responsibilities split into:
  - **Controller Layer** → Handles UI interaction, emits update signals to refresh views.
  - **Service Layer** → Contains all business logic, rules, and validations.
  - **Data Access Layer** → Manages database session and ORM models.
- This separation improves:
  - **Maintainability** (easier to update code without breaking other parts)
  - **Testability** (services can be tested independently)
  - **Scalability** (easy to add new features and modules)

### 🔄 Live UI Updates with PyQt5 Signals
- Introduced **real-time UI updates** using PyQt5 signals:
  - `books_updated` → Emitted when a book is **added, removed, loaned, or returned**.
  - `members_updated` → Emitted when a member is **added or removed**.
- **No more manual window reloads** — tables refresh instantly.

### 🛠 CLI Commands
We’ve added **console entry points** for easier management:

| Command                | Description |
|------------------------|-------------|
| `library-install`      | Creates and initializes the database |
| `library-run`          | Launches the Library Manager application |
| `library-uninstall`    | Drops the database |
| `setup-env`            | Creates the `.env` configuration file |
| `pip uninstall library_manager` | Uninstalls the package |

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

## 🏷 Version Tag
**Tag:** `v2.0.0`

---

💡 *With the new Service Layer architecture, the project is cleaner, more maintainable, and ready for future features like user authentication, advanced search, and reporting.*
