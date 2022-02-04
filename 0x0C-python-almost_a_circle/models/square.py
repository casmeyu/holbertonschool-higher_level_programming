#!/usr/bin/python3
"""Module for the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class thar inherits from Rectangle
        Attributes:
            id (int): id of the square
            __width (int): width of the square
            __height (int): height of the square
            __x (int): x position of the square
            __y (int): y position of the square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    # Built in functions
    def __str__(self):
        txt = f"[Square] ({self.id}) {self.x}/{self.y}"
        txt += f"{self.height}/{self.width}"
        return txt
