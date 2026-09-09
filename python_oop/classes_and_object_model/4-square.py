#!/usr/bin/env python3
"""This is a square. Fair and square."""


class Square:
    """Define Square constructor."""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    def get_size(self):
        return self.size

    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return self.size ** 2
