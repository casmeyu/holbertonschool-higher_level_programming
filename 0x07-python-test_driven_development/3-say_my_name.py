#!/usr/bin/python3
"""say may name
prints <first_name> <last_name>
"""


def say_my_name(first_name, last_name=""):
    """Prits the complete name
    Attributes:
        first_name (str): name to print
        las_name (str): last name to print
    """
    msg = ""
    if (type(first_name) is not str):
        raise TypeError("first_name must be a string")

    if (type(last_name) is not str):
        raise TypeError("last_name must be a string")

    msg += first_name
    if (len(last_name) > 0):
        msg += " {}".format(last_name)

    print(msg)
