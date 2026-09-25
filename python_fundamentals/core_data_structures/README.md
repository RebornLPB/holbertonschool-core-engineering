# Python - Core Data Structures

## Description
This project covers Python's core data structures: lists, tuples, sets, and dictionaries. Each script implements a small, self-contained function that reads, updates, or combines one of these structures.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Access, update, and print elements of a `list`, including 2D matrices.
* Combine and compare values in `tuple`s and `set`s.
* Look up and update key/value pairs in a `dict`.
* Handle out-of-range indices and empty containers safely.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `element_at.py` | Access a list element safely | Defines `element_at(my_list, idx)`, returning the element at `idx`, or `None` if the index is out of range. |
| `replace_in_list.py` | Replace a list element | Defines `replace_in_list(my_list, idx, element)`, replacing the element at `idx` if valid. |
| `print_list_integer.py` | Print a list of integers | Defines `print_list_integer(my_list=[])`, printing one integer per line. |
| `print_matrix_integer.py` | Print a matrix of integers | Defines `print_matrix_integer(matrix=[[]])`, printing each row space-separated. |
| `add_tuple.py` | Add two tuples | Defines `add_tuple(tuple_a=(), tuple_b=())`, summing two 2-value tuples element-wise (missing values default to 0). |
| `common_elements.py` | Find common elements between two sets | Defines `common_elements(set_1, set_2)`, returning their intersection. |
| `update_dictionary.py` | Update a dictionary | Defines `update_dictionary(a_dictionary, key, value)`, setting `key` to `value`. |
| `best_score.py` | Find the key with the biggest value | Defines `best_score(a_dictionary)`, returning the key with the highest value, or `None` if empty. |

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
