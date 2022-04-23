#!/usr/bin/python3
"""This Script sends an http request with urllib and prints some information"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as res:
        data = res.read()
        message = "Body response:\n\
\t- type: {}\n\
\t- content: {}\n\
\t- utf8 content: {}".format(type(data), data, data.decode('utf-8'))
        # message = f"Body response: type: {type(data)} - content: {data}"
        # why in the hell is the f"String" throws a Syntax Error!?!?
        print(message)
