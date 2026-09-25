# Python - Functions and Modules

## Description
This project covers writing reusable Python functions, organizing them into modules, and importing code between files. It illustrates the `if __name__ == "__main__":` guard, importing specific names with `from module import name`, and importing an entire module for its side effects.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Write functions with default parameter values and return values.
* Organize code into modules and import them (`import module`, `from module import name`).
* Understand the difference between running a script directly and importing it as a module.
* Use character codes (`ord`, `chr`) to implement custom case-conversion logic.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `add_0.py` | Simple addition | Defines `add(a, b)`, returning the sum of two numbers. |
| `add.py` | Import `add` | Imports `add` from `add_0` and prints the result of `add(1, 2)`. |
| `calculator_1.py` | Basic calculator functions | Defines `add`, `sub`, `mul`, and `div` for basic arithmetic. |
| `calculation.py` | Import the calculator functions | Imports and calls all four functions from `calculator_1` with two fixed values. |
| `islower.py` | Check for lowercase character | Defines `islower(c)`, returning `True` if `c` is a lowercase letter. |
| `uppercase.py` | Print in uppercase | Defines `uppercase(str)`, printing the given string converted to uppercase using character codes. |
| `pow.py` | Power function | Defines `pow(a, b)`, computing `a` to the power of `b` (supports negative exponents). |
| `print_last_digit.py` | Print the last digit of a number | Defines `print_last_digit(number)`, printing and returning its last digit. |
| `variable_load_5.py` | Load 98 | Defines a module-level variable `a = 98`. |
| `variable_load.py` | Import a variable | Imports `a` from `variable_load_5` and prints it. |
| `simple_add.py` | Minimal add & print | Defines `add(a, b)` and immediately prints `add(3, 5)`. |
| `test_import.py` | Import a module for its side effects | Imports `simple_add`, triggering its top-level `print` call. |

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
