#!/bin/bash
# Sends a Post request with the contents of a json file
curl -X POST -H 'Content-Type: application/json' -d @$2 $1
