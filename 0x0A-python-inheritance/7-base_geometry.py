#!/usr/bin/python3
"""Module base for BaseGeometry"""


class BaseGeometry():
    """BaseGeometry Class"""
    def area(self):
        """returns the area of the object"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
