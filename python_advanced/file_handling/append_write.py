#!/usr/bin/env python3
"""Module write_file
Reading and writing a file with append in python for the first time"""


def append_write(filename="", text=""):
    """Append a file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
