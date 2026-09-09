#!/usr/bin/env python3
"""This is a square. Fair and square."""


class Square:
    """Define Square constructor."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        self.check_size_value(value)
        self.__size = value

    def check_size_value(value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.check_size_value(value)
        self.__size = value

    def area(self):
        return self.size ** 2
