#!/usr/bin/python3
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

    def area(self):
        """int: eturns the area of the square"""
        return(self.__size**2)
