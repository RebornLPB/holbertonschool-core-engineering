# Python - Exception Handling

## Description
This project covers raising and safely catching exceptions in Python using `try`/`except`/`finally`. Each script demonstrates either explicitly raising an error or gracefully handling one so the program keeps running.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Raise built-in exceptions (`TypeError`, `NameError`) with `raise`.
* Catch specific exception types with `except (TypeError, ValueError)`.
* Use `finally` to guarantee code runs regardless of whether an exception occurred.
* Return sensible fallback values instead of letting a program crash.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `raise_exception.py` | Raise a TypeError | Defines `raise_exception()`, always raising a `TypeError`. |
| `raise_exception_msg.py` | Raise a NameError with a message | Defines `raise_exception_msg(message="")`, raising a `NameError` with the given message. |
| `safe_print_list.py` | Safely print list elements | Defines `safe_print_list(my_list=[], x=0)`, printing up to `x` elements and returning how many were printed, stopping on `IndexError`. |
| `safe_print_integer.py` | Safely print an integer | Defines `safe_print_integer(value)`, returning `True` on success or `False` if `value` cannot be formatted as an integer. |
| `safe_print_list_integers.py` | Safely print integers from a list | Defines `safe_print_list_integers(my_list=[], x=0)`, printing up to `x` integers, skipping non-integer values. |
| `safe_print_division.py` | Safely execute a division | Defines `safe_print_division(a, b)`, returning `None` on a division error while always printing the result via `finally`. |

---

## 🚀 Execution & PEP 8 Testing

```bash
chmod +x <file>.py
./<file>.py
```

```bash
pycodestyle <file>.py
```

---

## 👤 Author
* **Student:** [RebornLPB](https://github.com/RebornLPB)
* **GitHub:** [https://github.com/RebornLPB](https://github.com/RebornLPB)
* **School:** [Holberton School](https://www.holbertonschool.com/)
