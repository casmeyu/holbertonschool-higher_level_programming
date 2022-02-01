#!/usr/bin/python3
"""Module for saving a json object into a file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes the json representation of an object into a file
        Arguments:
            my_obj (object): object to parse into json
            filename (str): file to write the json representation
    """
    with open(filename, 'w+') as f:
        f.write(json.dumps(my_obj))
