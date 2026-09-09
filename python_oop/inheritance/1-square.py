#!/usr/bin/env python3

"""Module 1-square
Creation of Square class from the Rectangle module
"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle"""
    def __init__(self, size):
        self.integer_validator("Square", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
