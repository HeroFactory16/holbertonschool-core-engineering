#!/usr/bin/env python3
"""This is a square. Fair and square."""


class Square:
    """Define Square constructor."""

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) is not tuple or len(value) != 2 or
                not all(type(n) is int and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def get_size(self):
        return self.__size

    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        print(str(self))

    def __str__(self):
        if self.__size == 0:
            return ""
        lines = ["" for _ in range(self.__position[1])]
        lines += [" " * self.__position[0] + "#" * self.__size
                  for _ in range(self.__size)]
        return "\n".join(lines)
