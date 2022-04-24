#!/usr/bin/python3
"""Displays the header of an HTTP response"""
import requests
from sys import argv


if __name__ == '__main__':
    res = requests.get(argv[1])
    print(res.headers.get('X-Request-Id'))
