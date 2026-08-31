#!/usr/bin/env python3

def pow(a, b):
    if b < 0:
        value = 1
        for i in range(-b):
            value = value * a
        return 1 / value

    value = 1
    for i in range(b):
        value = value * a
    return value
