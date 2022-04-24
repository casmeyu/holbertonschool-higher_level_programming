#!/usr/bin/python3
# Uses the github api to get last 10 commits from a given repo
import requests
from sys import argv


max_commits = 10
req = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
req = request.Request(req)
req.add_header('accept', 'application/vnd.github.v3+json')

with request.urlopen(req) as res:
    data = res.read().decode('utf-8')
    data = json.loads(data)
    cont = 0
    for commit in data:
        m = "{}: {}".format(commit['sha'], commit['commit']['author']['name'])
        print(m)
        cont += 1
        if cont >= max_commits:
            break
