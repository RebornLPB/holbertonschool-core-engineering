#!/usr/bin/env python3


def islower(c):
    code = ord(c)
    if len(c):
        code = ord(c)
        if 65 <= code <= 90:
            return False
        elif 97 <= code <= 122:
            return True
