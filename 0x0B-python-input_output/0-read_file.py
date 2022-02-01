#!/usr/bin/python3
"""Module for reading a file"""


def read_file(filename=''):
    """This function opens a file and prints its content
        Arguments:
            file_name (str): file to read
    """
    with open(filename) as f:
        for line in f:
            print(line, end='')
