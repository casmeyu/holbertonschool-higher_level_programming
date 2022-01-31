#!/usr/bin/include
"""Module to check if an object inherits from a class"""


def inherits_from(obj, a_class):
    """Checks if obj iherits from a_class
        Arguments:
            obj: object to check
            a_class: class to check against
    """
    return (issubclass(type(obj), a_class))
