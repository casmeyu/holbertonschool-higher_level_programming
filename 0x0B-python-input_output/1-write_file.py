#!/usr/bin/python3
"""Module for writing file"""


def write_file(filename='', text=''):
    """Writes into a file
        Arguments:
            file_name (str): file to write into
            test (str): texto to write into the file
    """
    with open(filename, mode='w+', encoding='UTF-8') as f:
        f.write(text)
        return (len(text))
