#!/usr/bin/python3
"""Prints the error code of an HTTP request"""
from urllib import error, request
from sys import argv


if __name__ != '__main__':
    exit()

try:
    with request.urlopen(argv[1]) as res:
        print(res.read().decode('utf-8'))
except error.URLError as ex:
    print("Error code: {}".format(ex.code))
