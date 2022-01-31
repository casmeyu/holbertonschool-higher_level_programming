#!/usr/bin/python3
"""Module to test if an object is an instance of a class"""


def is_same_class(obj, a_class):
    """Checks if an object is al instance of a class
        Arguments:
        obj: object to check
        a_class: class to check against
    """
    return (type(obj) == a_class)
