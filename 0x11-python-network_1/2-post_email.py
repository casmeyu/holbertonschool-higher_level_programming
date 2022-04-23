#!/usr/bin/python3
# Send a POST request with urllib: request and parse
from urllib import parse, request
from sys import argv


if __name__ != '__main__' or len(argv) < 3:
    exit()

url = argv[1]
values = {'email': argv[2]}

# Parsing the dict into a POST format
post_data = parse.urlencode(values)
post_data = post_data.encode('utf-8')

# Concatenating the original url with the parsed values
parsed_url = request.Request(url, post_data)

with request.urlopen(parsed_url) as res:
    data = res.read().decode(res.headers.get_content_charset())
    print(data)
