#!/usr/bin/env python3

"""Module 1-rectangle
Creation of Rectangle class from the base_geometry module
"""


BaseGeometry = __import__('base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry"""
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, "Rectangle", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "Rectangle", height):
            self.__height = height
