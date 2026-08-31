#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for letter in str:
        code = ord(letter)
        if 97 <= code <= 122:
            result += chr(code - 32)
        else:
            result += letter

    print("{}".format(result))
