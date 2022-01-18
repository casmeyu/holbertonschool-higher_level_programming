#!/usr/bin/python3
"""
This is a square module
"""


class Square():
    """Description of Square class/object

    A simple square made out of hashs

    Attributes:
        __size (int): Size of the square

    """

    def check_values(self, size=1):
        """check if the __init__ values are correct"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """ size (int): size of the square. size >= 0

        """
        self.check_values(size)
        self.__size = size

    @property
    def size(self):
        """int: returns the size of the square"""
        return(self.__size)

    @size.setter
    def size(self, size=0):
        """int: sets size of the square"""
        self.check_values(size)
        self.__size = size

    def area(self):
        """int: eturns the area of the square"""
        return(self.__size**2)

    def __eq__(self, other):
        """compares if self == other according to area"""
        return(self.area() == other.area())

    def __ne__(self, other):
        """compares if self != other according to area"""
        return(self.area() != other.area())

    def __ge__(self, other):
        """compares if self >= other according to area"""
        return(self.area() >= other.area())

    def __gt__(self, other):
        """compares if self > other according to area"""
        return(self.area() > other.area())

    def __le__(self, other):
        """compares if self <= other according to area"""
        return(self.area() <= other.area())

    def __lt__(self, other):
        """compares if self < other according to area"""
        return(self.area() < other.area())
