# Python - Object-Oriented Programming

## Description
This project covers Python's object model: defining classes, encapsulating attributes with properties, building a class hierarchy through inheritance, and using abstract base classes and mixins to share behaviour between unrelated classes.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Define classes with `__init__`, instance attributes, and methods.
* Encapsulate private attributes behind `@property` getters/setters with validation.
* Build class hierarchies with `super()` and understand the Method Resolution Order (MRO).
* Use `abc.ABC` and `@abstractmethod` to enforce a contract on subclasses.
* Combine mixins for multiple inheritance and override `list` built-in methods.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 Sub-Projects

| Directory | Description |
| :--- | :--- |
| [`classes_and_object_model`](classes_and_object_model/) | Progressive build-up of a `Square`/`Rectangle` class with validated properties. |
| [`inheritance`](inheritance/) | `BaseGeometry` → `Rectangle` → `Square` hierarchy and polymorphism basics. |
| [`abc`](abc/) | Abstract base classes, mixins, and overriding built-in `list` methods. |

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
