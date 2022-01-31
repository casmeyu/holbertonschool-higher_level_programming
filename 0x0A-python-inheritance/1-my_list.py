#!/usr/bin/python3
"""Model for class MyList based on list"""


"""My list class"""


class MyList(list):
    """print_sorted - prints the list but sorted"""
    def print_sorted(self):
        for item in self:
            if type(item) != int:
                raise TypeError("must be a list of integers")
        print(sorted(self))
