#!/usr/bin/python3
"""Sends a POST request with a letter as parameter
If the response is JSON and not empty display [id] name"""
import requests
from sys import argv


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ''}

    if len(argv) > 1:
        values['q'] = argv[1]

    res = requests.post(url, data=values)
    data = res.json()
    try:
        print('[{}] {}'.format(data['id'], data['name']))
    except KeyError as ex:
        print('No result')
