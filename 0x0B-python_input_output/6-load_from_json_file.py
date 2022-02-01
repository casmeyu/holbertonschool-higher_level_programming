#!/usr/bin/python3
"""Moduel for reading a json file"""
import json


def load_from_json_file(filename):
    """Reads objects from a json file
        Arguments:
            filename (str): path of the file to read
    """
    with open(filename) as f:
        return (json.load(f))
