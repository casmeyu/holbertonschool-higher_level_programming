#!/usr/bin/python3
from sys import stderr


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        if (i > a):
            raise(Exception, "Too far")
        else:
            result += (b ** a) / i

    result += a + b
    return(result)
