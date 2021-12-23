#!/usr/bin/python3
import sys, hidden_4
for item in dir(hidden_4):
    if (item[0] != "_" or item[1] != "_"):
        print(item)
