#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Let's make a zoo!"""


class Animal(ABC):
    """Blueprint for all animals"""
    def __init__(self):
        pass

    @abstractmethod
    def sound(self):
        """Every animal has its own sound"""
        pass


class Dog(Animal):
    """Is a good boy"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """The true owner of the house"""
    def sound(self):
        return "Meow"
