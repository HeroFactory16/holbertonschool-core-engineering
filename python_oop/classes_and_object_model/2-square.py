#!/usr/bin/env python3
"""This is a square. Fair and square."""


class Square:
    """Define Square constructor."""

    def __init__(self, size):
        if size is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
