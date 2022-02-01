#!/usr/bin/python3
"""Module for the student class"""


class Student():
    """Student class for exercise
        Arguments:
            first_name (str): name of the student
            last_name (str): last name of the student
            age (int): age of the student
    """
    def __init__(self, first_name, last_name, age):
        """Object initialization
            Arguments:
                first_name (str): name of the student
                last_name (str): last name of the student
                age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary of attributes of self"""
        res = {}
        if not attrs:
            return (self.__dict__)
        else:
            for key in self.__dict__:
                if (type(key) is not str):
                    return (self.__dict__)
                if key in attrs:
                    res[key] = self.__dict__[key]
            return (res)
