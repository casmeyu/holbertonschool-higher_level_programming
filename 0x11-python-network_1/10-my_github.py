#!/usr/bin/python3
"""Takes github credentials and through the github api shows my id"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=(argv[1], argv[2]))
    try:
        data = res.json()
        print(data.get('id'))
    except Exception as ex:
        print('Not a valid JSON')
