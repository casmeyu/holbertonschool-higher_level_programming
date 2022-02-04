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
    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    # Built in functions
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of Square
            Arguemnts:
                size (int): must be >= 0
                x (int): must be > 0
                y (int): msut be > 0
                id (int): must be > 0
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        txt = f"[Square] ({self.id}) {self.x}/{self.y}"
        txt += f"{self.height}/{self.width} - {self.width}"
        return txt
