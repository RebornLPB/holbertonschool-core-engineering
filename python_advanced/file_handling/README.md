# Python - File Handling

## Description
This project covers reading from and writing to text files in Python using the `with` statement, which guarantees that file handles are properly closed. Each function opens a file with explicit UTF-8 encoding and performs a single, focused operation.

All scripts are written for **Python 3.8+** and follow the **PEP 8** style guide.

## 📝 Learning Objectives
* Open a file for reading, writing, or appending with `open()`.
* Use the `with` statement to manage file resources safely.
* Explicitly set the file encoding (`utf-8`) to avoid platform-dependent behaviour.
* Understand the difference between the `"r"`, `"w"`, and `"a"` file modes.

## 🛠️ Requirements & Engineering Constraints
* **OS:** Ubuntu 20.04 LTS
* **Interpreter:** `python3` (version 3.8.5+)
* **Style Guide:** 100% compliant with PEP 8 standards (verified via `pycodestyle`).
* **Execution:** All Python files are executable (`chmod +x`) and start with `#!/usr/bin/env python3`.

## 📁 File List & Tasks Directory

| File | Task Title | Description |
| :--- | :--- | :--- |
| `read_file.py` | Read a file | Defines `read_file(filename="")`, reading a UTF-8 text file and printing its content to stdout. |
| `write_file.py` | Write to a file | Defines `write_file(filename="", text="")`, overwriting the file with `text` and returning the number of characters written. |
| `append_write.py` | Append to a file | Defines `append_write(filename="", text="")`, appending `text` to the end of the file and returning the number of characters written. |

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
