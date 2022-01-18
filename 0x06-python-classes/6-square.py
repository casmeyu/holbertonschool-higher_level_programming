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

    def check_values(self, size=0, position=(0, 0)):
        """check if the __init__ values are correct"""
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (isinstance(position, (int, int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        """ size (int): size of the square. size >= 0
            position (tuple): position of the square. position >= (0, 0)

        """
        self.check_values(size, position)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: returns the size of the square"""
        return(self.__size)

    @size.setter
    def size(self, size=0):
        """int: sets size of the square"""
        self.check_values(size, None)
        self.__size = size

    @property
    def position(self):
        """tuple: returns the position of the square"""
        return(self.__position)

    @position.setter
    def position(self, value):
        """tuple: sets position of the square"""
        self.check_values(None, position)
        self.__position = position

    def area(self):
        """int: eturns the area of the square"""
        return(self.__size**2)

    def my_print(self):
        """prins the square on the terminal"""
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for line in range(self.__size):
                for i in range(self.__position[0]):
                    print("_", end='')
                for col in range(self.__size):
                    print("#", end='')
                print()
