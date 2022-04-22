#!/bin/bash
# Prints the lenght of an http response
if [ $1 ]
then
  curl -s $1 | wc -c
fi
