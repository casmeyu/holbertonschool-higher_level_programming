#!/usr/bin/python3
"""Module to check if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """checks if and object is instance of class
        Arguments:
            obj: object to check
            a_class: class to check against
    """
    return (isinstance(obj, a_class))
