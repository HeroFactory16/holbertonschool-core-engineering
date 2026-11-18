#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""Did you say DRAGON???"""


class SwimMixin:
    """Toolbox with palms or something"""
    def __init__(self):
        pass

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Toolbox with wings or something"""
    def __init__(self):
        pass

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Ooooh yeah, you meant DRAGON"""
    def __init__(self):
        pass

    def roar(self):
        print("The dragon roars!")
