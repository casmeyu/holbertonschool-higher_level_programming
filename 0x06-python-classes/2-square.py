#!/usr/bin/python3
"""
This is a square module
"""


class Square():
    """Description of Square class/object

    A simple square made out of hashs

    Attributes:
        __size (int): Size of the square
        __position (tuple): Position of the square relative to top-left

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
        self.check_values(size, None)
        self.__size = size
