#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi
"""Let's make a bit of geometry"""


class Shape(ABC):
    """Basic blueprint for all shapes"""
    def __init__(self):
        pass

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def shape_info(self):
        print(f"Area: {self.area}\nPerimeter: {self.perimeter}")

    @abstractmethod
    def area(self):
        """Each shape must compute its own area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Each shape must compute its own perimeter"""
        pass


class Circle(Shape):
    """Reject pointy guy, go back round"""
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * (self.__radius ** 2)

    def perimeter(self):
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """I believe in right-angled corner supremacy"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)
