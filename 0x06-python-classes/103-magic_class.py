#!/usr/bin/python3

"""Creates a magic cirle"""
import math


class MagicClass:
    """Class: magic circle"""
    def __init__(self, radius=0):
        """constructor method"""
        self.__radius = 0
        if type(radius) is not int:
            if type(radius) is not float:
                raise TypeError("radius must be a number")
        self.__radius = radius
        return None

    def area(self):
        """calculates area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """calculates the circumference"""
        return (2 * math.pi) * self.__radius
