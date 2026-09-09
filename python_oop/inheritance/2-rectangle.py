#!/usr/bin/env python3

"""Module 2-rectangle
Creation of Rectangle class from the base_geometry module
"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator("Rectangle", width)
        self.__width = width
        self.integer_validator("Rectangle", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
