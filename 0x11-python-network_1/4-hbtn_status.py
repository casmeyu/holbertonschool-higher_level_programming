#!/usr/bin/python3
"""This Script sends an http request with urllib and prints some information"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as res:
        data = res.read().decode('utf-8')
        message = "Body response:\n\
\t- type: {}\n\
\t- content: {}".format(type(data), data)
        print(message)
