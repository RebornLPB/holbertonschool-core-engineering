#!/usr/bin/env python3

def uppercase(str):
	result = ""
	for letter in str:
		code = ord(letter)
		calc = code - 32
		result += chr(calc)

	print("{}".format(result), end="")
