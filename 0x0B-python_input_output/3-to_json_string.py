#!/usr/bin/python3
"""Module for json to string"""
import json


def to_json_string(my_obj):
    """Returns an object converted into json
        Arguments:
            my_obj (object): object to parse
    """
    return (json.dumps(my_obj))
