#!/usr/bin/env python3


def islower(c):
    code = ord(c)
    if len(c):
        code = ord(c)
        if 65 <= code <= 90:
            print(f"'{c}' est une majuscule.")
        elif 97 <= code <= 122:
            print(f"'{c}' est une minuscule.")
