#!/usr/bin/python3
"""Sends a POST http request with an email loaded as a value"""
import requests
from sys import argv


if __name__ == '__main__':
    values = {'email': argv[2]}
    res = requests.post(argv[1], data=values)
    print(res.text)
