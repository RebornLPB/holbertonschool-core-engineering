#!/usr/bin/env python3

"""Module 2-square
Creation of Square class from the Rectangle module
"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square class from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
            return "[Square] {}/{}".format(self.__size, self.__size)
