#!/usr/bin/python3
"""Module for square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Initializes the square with a positive size"""
        Rectangle.integer_validator(self, 'size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Prints the square"""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
