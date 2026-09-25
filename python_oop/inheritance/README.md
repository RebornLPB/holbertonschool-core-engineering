# Python - Inheritance

## Description
This project covers class inheritance and polymorphism. It starts with a simple `Animal`/`Dog`/`Cat` polymorphism demo, then builds a `BaseGeometry` → `Rectangle` → `Square` hierarchy where each subclass reuses and extends the validation logic of its parent through `super()`.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Override a parent method in a subclass (polymorphism).
* Check types and hierarchies with `isinstance()` and `issubclass()`.
* Share a common validator (`integer_validator`) across a class hierarchy.
* Call a parent's `__init__` with `super().__init__()` to avoid duplicating logic.
* Implement `__str__` to control how instances are printed.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `0-polymorphism_demo.py` | Polymorphism demo | `Animal`, `Dog`, and `Cat` each override `speak()`; demonstrates `isinstance()` and `issubclass()`. |
| `base_geometry.py` | Base geometry class | `BaseGeometry` provides an unimplemented `area()` and a reusable `integer_validator(name, value)`. |
| `1-rectangle.py` | Inherit from BaseGeometry | `Rectangle(BaseGeometry)` validates and stores `width`/`height`. |
| `2-rectangle.py` | Rectangle area and string | Adds `area()` and `__str__` (`"[Rectangle] width/height"`) to `Rectangle`. |
| `1-square.py` | Square #1 | `Square(Rectangle)` reuses `Rectangle.__init__` via `super()` and adds `area()`. |
| `2-square.py` | Square #2 | Adds `__str__` (`"[Square] size/size"`) to `Square`. |

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
