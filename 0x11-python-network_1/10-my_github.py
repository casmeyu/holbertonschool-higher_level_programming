#!/usr/bin/python3
"""Takes github credentials and through the github api shows my id"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    res = requests.get(url, auth=(argv[1], argv[2]))
    data = res.json()
    try:
        print(data['id'])
    except KeyError as ex:
        print('None')
