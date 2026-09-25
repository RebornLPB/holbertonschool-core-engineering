# Python - Debugging Strategies

## Description
This project is a series of small, intentionally-broken scripts used to practice different debugging techniques: reading the traceback/code, adding temporary `print()` calls, stepping through with `pdb`, tracing data across multiple functions, using the `logging` module, and writing defensive code that validates its inputs. Each script's top comment block documents the bug found and the fix applied.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Read a traceback and locate the faulty line before touching any code.
* Use temporary `print()` statements to inspect state during execution.
* Set a breakpoint and step through code with `pdb`.
* Trace how bad data propagates across several functions to find its origin.
* Replace ad-hoc prints with leveled `logging` calls (`debug`, `info`, `warning`).
* Write defensive code that validates arguments and fails predictably instead of crashing.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-reading.py` | Reading the bug | Sums sensor readings; bug was summing a `str` value into an `int` — fixed with `int(value)`. |
| `1-print.py` | Debugging with print() | Counts readings at/above a threshold; bug was using `<` instead of `>=` in the comparison. |
| `2-pdb.py` | First steps with pdb | Computes an adjusted average; bug was accumulating the raw score instead of the adjusted one, found via `pdb`. |
| `3-data.py` | Following the data | Computes a cart total after discount; bug traced through several functions to `parse_discount_rate`, which returned a percentage instead of a decimal rate. |
| `4-logging.py` | Debugging with logging | Computes an average over valid sensor records; bug was incrementing the counter outside the validity check, found using `logging`. |
| `5-defensive.py` | Defensive programming | Hardens `compute_average_valid` against `None`/wrong-type input, non-dict records, and empty lists to avoid crashes (`TypeError`, `ZeroDivisionError`). |

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
