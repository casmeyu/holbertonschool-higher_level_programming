#!/usr/bin/python3
"""Module to check if an object inherits from a class"""


def inherits_from(obj, a_class):
    """Checks if obj iherits from a_class
        Arguments:
            obj: object to check
            a_class: class to check against
    """
    if (type(obj) == a_class):
        return False
    return (issubclass(type(obj), a_class))
