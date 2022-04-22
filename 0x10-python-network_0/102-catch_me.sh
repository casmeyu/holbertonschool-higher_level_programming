#!/bin/bash
# Sends a request to catch a killer
curl -sL -X PUT -F "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
