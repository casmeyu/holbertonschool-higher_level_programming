#!/usb/bin/python3
"""Lookupmodule
prints information about objects
"""


def lookup(object):
    """returns a list with all the object attributes"""
    return dir(object)
