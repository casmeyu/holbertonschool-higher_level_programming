#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    def __eq__(self, obj):
        if self is not obj:
            return False
        return True

    def __ne__(self, obj):
        if self is obj:
            return False
        return True
