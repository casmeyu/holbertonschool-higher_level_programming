#!/usr/bin/python3
""" test for locked attributes for a class"""


class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        pass
