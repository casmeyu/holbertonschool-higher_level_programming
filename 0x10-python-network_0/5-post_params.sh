#!/bin/bash
# Sends a POST request to a server with data
curl -s -X POST -F 'email=test@gmail.com' -F 'subject=I will always be here for PLD' $1
