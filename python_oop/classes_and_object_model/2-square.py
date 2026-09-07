#!/usr/bin/env python3

"""
Module 1-square
Second class made so far
"""


class Square:
    """Second class made so far"""
    def __init__(self, size):
        if isinstance(size, int) == False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
