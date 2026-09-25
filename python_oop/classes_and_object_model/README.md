# Python - Classes and Object Model

## Description
This project builds a `Square` (and a companion `Rectangle`) class step by step, from an empty class to a fully validated object with computed attributes (`area`, `my_print`, `__str__`) and a printable representation. Each numbered file adds one new capability on top of the previous one.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Define a class with `__init__` and private (name-mangled) instance attributes.
* Protect attributes with `@property` getters and validating setters.
* Raise `TypeError`/`ValueError` for invalid attribute assignments.
* Add computed methods (`area`, `perimeter`) and a custom `__str__` representation.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-square.py` | My first square | Empty `Square` class with just an `__init__`. |
| `1-square.py` | Square with size | `Square` stores a private `__size` attribute. |
| `1-rectangle.py` | My first rectangle | `Rectangle` with `width`/`height` properties, each validated (must be a non-negative `int`). |
| `2-square.py` | Size validation | `Square.__init__` validates `size` is a non-negative `int`. |
| `2-rectangle.py` | Area and perimeter | Adds `area()` and `perimeter()` to `Rectangle`. |
| `3-square.py` | Area | Adds `area()` to `Square`. |
| `4-square.py` | Size as a property | Turns `size` into a validated `@property`. |
| `5-square.py` | My print | Adds `my_print()`, printing the square as a grid of `#`. |
| `6-square.py` | Position | Adds a `position` property (2-tuple of non-negative ints) and a `__str__` that renders the square offset by that position. |

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
