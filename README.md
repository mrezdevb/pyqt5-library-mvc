# 📚 Library Manager — Release v2.2.0

## 🚀 What's New in This Release

### 🏗 Professional Project Structure
- The project is reorganized into a **clear and maintainable layout**:
```
app/
├── controllers/       # Handles UI events and user interaction
├── services/          # Contains business logic and rules, manages database access
├── models/            # SQLAlchemy ORM models
├── observability/     # Logging, trace IDs, and helpers
├── db/                # Database initialization and session
├── ui/                # PyQt5 UI actions and widgets
└── views/             # PyQt5 window layouts and forms

assets/               # Images and static assets
scripts/              # CLI entry points for install, uninstall, setup-env
tests/                # Unit and integration tests
```

### 🕵️‍♂️ Advanced Observability
- **Trace ID System**
  - Each action is tagged with a **unique Trace ID** for debugging and monitoring.
  - Works for all CRUD operations on books and members.
- **JSON Log Export**
  - Logs can now be saved in **JSON format** for auditing or persistent storage.
  - Makes debugging and analytics straightforward.

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

## 🏷 Version Tag
**Tag:** `v2.2.0`

---
- Update your `.env` if migrating from v2.2.0.  
- Old logs may require conversion to JSON format to use new export feature.
