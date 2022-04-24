#!/usr/bin/python3
"""Uses the github api to get last 10 commits from a given repo"""
import requests
from sys import argv


max_commits = 10
cont = 0
url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
res = requests.get(url)
data = res.json()
for c in data:
    msg = "{}: {}".format(c['sha'], c['commit']['author']['name'])
    print(msg)
    cont += 1
    if cont >= max_commits:
        break
