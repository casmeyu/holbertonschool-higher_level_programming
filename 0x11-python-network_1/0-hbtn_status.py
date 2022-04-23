#!/usr/bin/env python3
"""This Script sends an http request with urllib and prints some information"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://intranet.hbtn.io/status') as res:
        data = res.read()
        message = "Body response:\n\
\t- type: {}\n\
\t- content: {}".format(type(data), data)
        # message = f"Body response: type: {type(data)} - content: {data}"
        # why in the hell is the f"String" throws a Syntax Error!?!?
        if res.headers.get_content_charset() == 'utf-8':
            message += '\n\t- utf8 content: OK'
        print(message)
