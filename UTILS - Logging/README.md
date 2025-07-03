# Logging Utilities

This project provides simple logging utilities in both Python and JavaScript. You can add, read, edit, and delete log entries using either language. All logs are stored in a file named `log.txt` in the same directory.

---

## Python Logger

### Requirements
- Python 3.x (no external libraries required)

### Installation
No installation is required for Python. Just ensure you have Python 3 installed.

### Usage
1. Place `logger.py` in your project directory.
2. Run the logger with:
   ```sh
   python logger.py
   ```
3. You will see a menu:
   - Add log entry
   - Read all log entries
   - Edit a log entry
   - Delete a log entry
   - Exit
4. Follow the prompts to manage your log entries interactively.

---

## JavaScript Logger

### Requirements
- Node.js
- `readline-sync` package (for interactive CLI)

### Installation
1. Place `logger.js` in your project directory.
2. Install the required package (only needed once):
   ```sh
   npm install readline-sync
   ```

### Usage
1. Run the logger with:
   ```sh
   node logger.js
   ```
2. You will see a menu:
   - Add log entry
   - Read all log entries
   - Edit a log entry
   - Delete a log entry
   - Exit
3. Follow the prompts to manage your log entries interactively.

---

## Notes
- Both loggers use the same `log.txt` file by default. If you use both in the same directory, they will operate on the same log file.
- All functions are commented for clarity.

---

## License
This project is open source and free to use. 