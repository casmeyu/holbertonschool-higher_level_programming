#!/usr/bin/python3
"""Module for the student class"""
import json


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
        print(self)

    def to_json(self, attrs=None):
        """Returns the dictionary of attributes of self"""
        return (self.__dict__)
