#!/usr/bin/python3
"""Module for creating"""
import json


def from_json_string(my_str):
    """Returns an object based of a json string
        Arguments:
            my_str (str): json string to parse into object
    """
    return (json.loads(my_str))
