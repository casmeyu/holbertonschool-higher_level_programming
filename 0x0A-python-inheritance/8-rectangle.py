#!/usr/bin/python3
"""Module for Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Recntangle class
        Attributes:
            width (int)
            height (int)
    """
    def __init__(self, width, height):
        Rectangle.integer_validator(self, 'width', width)
        Rectangle.integer_validator(self, 'height', height)
        self.__height = height
        self.__width = width
