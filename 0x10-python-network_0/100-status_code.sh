#!/bin/bash
# Show the status code of a HTTP request
curl -s -o /dev/null -w "%{http_code}" $1
