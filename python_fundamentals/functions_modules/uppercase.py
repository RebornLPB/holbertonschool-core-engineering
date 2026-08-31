#!/usr/bin/env python3

def uppercase(str):
	result = ""
	for letter in str:
		code = ord(str)
		calc = code - 32
		result += chr(calc)

	print(f"{result}", end="")
