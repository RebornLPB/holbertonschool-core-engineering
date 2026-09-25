# Python - ABCs, Mixins & Multiple Inheritance

## Description
This project explores three different ways Python classes can share and enforce behaviour: abstract base classes (`abc.ABC`) that force subclasses to implement specific methods, mixins that add capabilities to unrelated classes, and overriding built-in `list` methods to add custom behaviour on top of the standard container.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Define an abstract base class with `abc.ABC` and `@abstractmethod`.
* Understand why an abstract class cannot be instantiated directly.
* Use mixin classes to add reusable behaviour (`swim`, `fly`) to otherwise unrelated classes.
* Inspect the Method Resolution Order with `ClassName.mro()`.
* Subclass a built-in type (`list`) and override its methods while still calling `super()`.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `animals.py` | Abstract Animal | `Animal(ABC)` declares the abstract method `sound()`; `Dog` and `Cat` implement it. |
| `shapes.py` | Abstract Shape | `Shape(ABC)` declares abstract `area()` and `perimeter()`; `Circle` and `Rectangle` implement them, plus a `shape_info()` helper to print both. |
| `flyingfish.py` | Multiple inheritance | `FlyingFish` inherits from both `Fish` and `Bird`, overriding `swim`, `fly`, and `habitat`; prints its own MRO. |
| `dragon.py` | Mixins | `SwimMixin` and `FlyMixin` are combined into a `Dragon` class that can swim, fly, and roar. |
| `verboselist.py` | Extending `list` | `VerboseList` overrides `append`, `extend`, `remove`, and `pop` to print a message on every mutation while still delegating to `list` via `super()`. |

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
