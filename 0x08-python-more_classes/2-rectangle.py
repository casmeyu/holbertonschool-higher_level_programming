#!/usr/bin/python3
"""This is the rectangle module"""


class Rectangle():
    """Rectangle class
    Arguments:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Constructor for a rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, width):
        """sets width of the rectangle
            width (int): must be >= 0
        """
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, height):
        """sets height of the rectangle
            height (int): must be >= 0
        """
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")

        self.__height = height

    # Class methods
    def area(self):
        """Returns the area of the rectangle"""
        return(self.height * self.width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return((self.height * 2) + (self.width * 2))
