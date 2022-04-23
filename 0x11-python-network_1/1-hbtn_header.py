#!/usr/bin/python3
"""This scripts returns the value of a specific Header value of http request"""
from urllib import request
from sys import argv


if __name__ == '__main__':
    if len(argv) > 1:
        with request.urlopen(argv[1]) as res:
            search = 'X-Request-Id'
            print(res.headers.get(search))
