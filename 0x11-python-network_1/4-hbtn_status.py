#!/usr/bin/python3
"""This Script sends an http request with urllib and prints some information"""
import requests


if __name__ == '__main__':
    res = requests.get('https://intranet.hbtn.io/status')
    message = "Body response:\n\
\t- type: {}\n\
\t- content: {}".format(type(res.text), res.text)
    print(message)
