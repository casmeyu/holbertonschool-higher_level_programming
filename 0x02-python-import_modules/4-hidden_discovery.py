#!/usr/bin/python3
import sys, hidden_4
if __name__ == "__main__":
    items = dir(hidden_4)
    items.sort()
    for item in items:
        if (item[0] != "_" and item[1] != "_"):
            print(item)
