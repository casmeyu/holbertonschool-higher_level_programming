#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return(False)
    except (TypeError, ValueError):
        return(False)
