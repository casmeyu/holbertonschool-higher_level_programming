#!/usr/bin/python3
""" test for locked attributes for a class"""


class LockedClass:
    """Class with resctricted attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Class initializator"""
        pass
