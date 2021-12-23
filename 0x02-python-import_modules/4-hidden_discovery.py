#!/usr/bin/python3
import sys, hidden_4
if __name__ == "__main__":
    for item in dir(hidden_4):
        if (item[:2]!= "__"):
            print(item)
