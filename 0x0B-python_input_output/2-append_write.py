#!/usr/bin/python3
"""Module for writing file"""


def append_write(filename='', text=''):
    """Appends text into a file
        Arguments:
            file_name (str): file to write into
            test (str): texto to write into the file
    """
    with open(filename, mode='a+', encoding='UTF-8') as f:
        f.write(text)
        return (len(text))
