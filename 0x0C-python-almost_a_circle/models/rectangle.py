#!/usr/bin/python3
"""This module is for the Rectangle class which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This is the Rectangle class with respective functions
        Attributes:
            __width (int): private width of the rectangle
            __height (int): private height of the rectangle
            __x (int): private x position
            __y (int): private y position
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of Rectangle object with respective size and position
            Arguments:
                width (int): must be > 0
                height (int): must be > 0
                x (int): must be >= 0
                y (int): must be >= 0
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, width):
        if (type(width) is not int):
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")

        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, height):
        if (type(height) is not int):
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")

        self.__height = height

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, x):
        if (type(x) is not int):
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")

        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) is not int):
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")

        self.__y = y

    # Built in functions
    def __str__(self):
        txt = f"[Rectangle] ({self.id}) {self.x}/{self.y}"
        txt += f" {self.width}/{self.height}"
        return (txt)

    # Rectangle Functionality
    def area(self):
        """Returns the area of the rectangle (int)"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle on the console"""
        for line in range(self.__height):
            print('#'*self.__width)
