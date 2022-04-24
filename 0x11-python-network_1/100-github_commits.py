#!/usr/bin/python3
# Uses the github api to get last 10 commits from a given repo
import requests
from sys import argv


max_commits = 10
req = 'https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])
req = requests.Request(req)
req.add_header('accept', 'application/vnd.github.v3+json')

