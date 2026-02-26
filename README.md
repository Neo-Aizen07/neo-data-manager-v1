# Neo Data Manager v1.5 🗃️

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A privacy-first, offline CLI database management system built in Python. No cloud. No internet required. Your data stays on your machine.

---

## 📂 Project Structure

```
neo-data-manager/
├── main.py            # 🟢 Entry point, menu loop
├── RecordManager.py   # 🧠 Core brain, single source of truth for all state
├── storage.py         # 💾 Atomic save and load — self-healing JSON
├── operations.py      # ⚙️  Deletion logic
├── search.py          # 🔍 Search by ID or partial username
├── user_entry.py      # ⌨️  Registration and input handling
├── user_interface.py  # 🎨 ID generation, timestamps
├── Validation.py      # ✅ Username and name validation rules
├── logger.py          # 📋 Logging system with ISO timestamps
├── file_data.py       # 🛠️  File path diagnostics
└── data.json          # 📦 Local database (auto-created if missing)
```

---

## 🚀 What's New in v1.5

### Bug Fixes
- **Duplicate Username Fix:** Records were being silently overwritten due to a state management bug in `RecordManager.__init__`. Fixed by correcting how `file_load` assigns to `self.records`.
- **Mutable State Overhaul:** Removed scattered state across modules. `RecordManager` is now the single brain — all reads and writes go through it.
- **Atomic Save Stability:** Improved the temp file → `os.replace` pipeline to prevent corruption on interrupted writes.

### New Features
- **Partial Username Search:** Search by typing any part of a username. Returns all matches and lets you pick.
- **Standard Logging System:** Replaced custom logger with Python's `logging` library. ISO timestamp format. Logs saved to `error.log`.
- **Log Viewer Menu:** View today's logs or errors only directly from the CLI — no need to open the file manually.
- **Self-Healing Database:** If `data.json` is missing, it is automatically recreated on next save. Zero manual intervention needed.

### Removed
- QR code generation (removed for stability and scope focus)
- Search by full name (replaced with partial username search)

---

## ✨ Features

- **Fully Offline** — zero internet dependency, zero cloud
- **Persistent Storage** — JSON-based, survives restarts
- **Atomic Writes** — data written to temp file first, then replaced. Corruption resistant.
- **Self-Healing** — missing database file is recreated automatically
- **Unique ID Generation** — 10-character hex ID per record via `uuid`
- **Partial Search** — find users by partial username match
- **Validation** — strict username and name rules enforced before any record is created
- **Logging** — every action logged with ISO timestamp, level, and message

---

## 🛠️ Core Functions

| Function | File | Description |
|---|---|---|
| `name_enter()` | user_entry.py | Register new user with validation |
| `search_func()` | search.py | Search by ID or partial username |
| `delete_data()` | operations.py | Delete all records with confirmation |
| `delete_person()` | operations.py | Delete single user with confirmation |
| `file_load()` | storage.py | Load records from data.json |
| `save_names()` | storage.py | Atomic save to data.json |
| `log_menu()` | logger.py | View logs from CLI |
| `verify()` | file_data.py | Diagnose file paths and existence |

---

## ⚠️ Known Limitations

- **Single user only** — no concurrent access support
- **Manual JSON edits** — breaking the JSON syntax will cause load failure
- **No universal search** — must choose ID or username mode explicitly
- **No multi-field search** — cannot search by name, only username or ID

---

## 🛠️ Installation

```bash
git clone https://github.com/Neo-Aizen07/neo-data-manager.git
cd neo-data-manager
pip install -r requirements.txt
python main.py
```

---

## 📈 Version History

| Version | Highlights |
|---|---|
| v1.0 | Initial release, basic CRUD |
| v1.1 | Fixed logic errors, improved JSON serialization, UUID generation |
| v1.2 | Username indexing, UI processing effects |
| v1.3 | Validation fixes, keyboard QR close, separate delete operations |
| v1.4 | Data persistence fix, atomic saves, file verification, case-insensitive search |
| v1.5 | Duplicate username fix, partial search, standard logging, self-healing JSON, mutable state overhaul |

---

## 💡 Notes

- Code is written and debugged manually — AI used only for code review and README writing
- Contributions and feedback welcome
- Planned for v1.6: SQL migration via SQLite

---


