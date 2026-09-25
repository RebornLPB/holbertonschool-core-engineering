# Python - Environment & First Programs

## Description
This project introduces the fundamentals of setting up a Python development environment and executing basic Python programs. It covers formatting structured outputs and printing variables cleanly, while strictly adhering to the **PEP 8** style guide.

All scripts are written for **Python 3.8+**.

## 📝 Learning Objectives
* Set up and configure a Python 3 development environment on Linux.
* Execute Python code via script files with executable permissions.
* Format structured outputs using f-strings and `print`.
* Understand the importance of the **PEP 8** coding style and use `pycodestyle` for syntax checking.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** The Python file is executable (`chmod +x`) and starts with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `structured_output.py` | Structured Output | Declares a float and a boolean, then prints the language name, version, and formatted variables (`Pi approx`, `Computation valid`). |

---

## 🚀 Execution & PEP 8 Testing

### Running the Script
```bash
chmod +x structured_output.py
./structured_output.py
```

Or execute via the Python 3 interpreter:
```bash
python3 structured_output.py
```

### Checking PEP 8 Compliance
```bash
pycodestyle structured_output.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
