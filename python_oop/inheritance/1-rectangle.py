#!/usr/bin/env python3
"""Let's make a rectangle, shall we?"""


class BaseGeometry:
    """Class definition"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle definition"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
