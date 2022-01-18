#!/usr/bin/python3
class Square():
    def check_values(self, size=1, position=(0, 0)):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        if (type(position) != tuple or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, position=(0, 0)):
        self.check_values(size, position)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, size=0):
        self.check_values(size, None)
        self.__size = size

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        self.check_values(None, position)
        self.__position = position

    def area(self):
        return(self.__size**2)

    def my_print(self):
        if (self.__size == 0):
            print()
        for i in range(self.__position[1]):
            print()
        for line in range(self.__size):
            for i in range(self.__position[0]):
                print("_", end='')
            for col in range(self.__size):
                print("#", end='')
            print()
