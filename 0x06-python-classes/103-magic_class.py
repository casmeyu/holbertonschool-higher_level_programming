#!/usr/bin/python3
from dis import dis
"""Reverse engenieered from Python Bytecode"""


class MagicClass:
    """Class: Its a magic circle"""
    def __init__(self, radius=0):
        """Creation of the circle"""
        self.__radius = 0
        if (type(radius) is not int):
                if (type(radius) is not float):
                    raise TypeError("radius must be a number")
        
        self.__radius = radius
        

    def area(self):
        """Area of a circle"""
        return((self.___radius ** 2) * math.pi)

    def circumference(self, radius):
        """Circumference of the circle"""
        return (2 * math.pi) * self.__radius

print(dis(MagicClass))
