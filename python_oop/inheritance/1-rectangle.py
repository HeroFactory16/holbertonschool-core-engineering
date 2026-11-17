#!/usr/bin/env python3
from base_geometry import BaseGeometry
"""Let's make a rectangle, shall we?"""


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        if self.integer_validator(width):
            self.width = width
        if self.integer_validator(height):
            self.height = height
