#!/bin/bash
# Prints the lenght of an http response
curl -s $1 | wc -c
