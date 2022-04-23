#!/usr/bin/python3
"""This scripts returns the value of a specific Header value of http request"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io') as res:
        search = 'X-Request-Id'
        print(res.headers.get(search))
