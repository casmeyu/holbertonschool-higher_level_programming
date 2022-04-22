#!/bin/bash
# Prints all the allowed methods for the request
curl -is $1 | grep Allow: | cut -d' ' -f2-
