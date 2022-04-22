#!/bin/bash
if [ $1 ]
then
  curl -s $1 | wc -c
fi
