#!/usr/bin/env python3
"""This is a rectangle. Fair and rectangle... I guess"""

class Rectangle:
    """Define Rectangle constructor."""

    def __init__(self, width=0, height=0, position=(0, 0)):
        self.width = width
        self.height = height
        self.position = position

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

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

    def area(self):
        return self.width * self.height

    def my_print(self):
        print(str(self))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["" for _ in range(self.__position[1])]
        lines += [" " * self.__position[0] + "#" * self.__width
                  for _ in range(self.__height)]
        return "\n".join(lines)