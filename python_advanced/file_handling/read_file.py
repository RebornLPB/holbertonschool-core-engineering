#!/usr/bin/env python3
"""Module read_file
Reading file in python for the first time"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
