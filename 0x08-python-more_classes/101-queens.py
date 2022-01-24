#!/usr/bin/python3
import sys


def gambit_game(size):
    print("entered with {}".format(size))


if __name__ == '__main__':
    argc = len(sys.argv)
    if (argc != 2):
        print("Usage: nqueens N")
        exit(1)
    if (sys.argv[1].isdigit()):
        size = int(sys.argv[1])
        if (size >= 4):
            gambit_game(size)
        else:
            print("N must be at least 4")
            exit(1)
    else:
        print("N must be a number")
        exit(1)
