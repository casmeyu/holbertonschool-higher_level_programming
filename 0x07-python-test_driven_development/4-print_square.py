#!/usr/bin/python3
"""Printing square module"""


def print_square(size):
    """ prints a square of a given size
        Arguments:
            size (int): >= 0
    """
    if type(size) is not int:
        # if (type(size) is float): ? do i have to convert ?
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for line in range(size):
            for column in range(size):
                print("#", end='')
            print()
