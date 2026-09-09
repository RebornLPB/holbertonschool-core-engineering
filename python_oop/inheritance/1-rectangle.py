#!/usr/bin/env python3
from base_geometry import BaseGeometry

"""Module 1-rectangle
Creation of Rectangle class from the base_geometry module"""


class Rectangle(BaseGeometry):
    """Rectangle class from BaseGeometry"""
    def __init__(self, width, height):
        if BaseGeometry.integer_validator(self, "width", width):
            self.__width = width
        if BaseGeometry.integer_validator(self, "height", height):
            self.__height = height


