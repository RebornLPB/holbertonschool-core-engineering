#!/usr/bin/env python3
"""Module write_file
Reading and writing a file in python for the first time"""


def write_file(filename="", text=""):
    """Write a file."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{text}\n")
