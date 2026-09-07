#!/usr/bin/env python3

"""
Module 1-square
Second class made so far
"""


class Square:
    """Second class made so far"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
