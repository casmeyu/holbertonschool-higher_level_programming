#!/usr/bin/python3
"""Prints the response of and HTTP request or its Error Code if it failed"""
import requests
from sys import argv


if __name__ == '__main__':
    res = requests.get(argv[1])
    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
