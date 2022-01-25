#!/usr/bin/python3
def magic_string():
    # magic_string.i if hasattr(magic_string, "i") else magic_string.i = 1
    res = ""
    if hasattr(magic_string, "i"):
        magic_string.i += 1
    else:
        magic_string.i = 1

    for x in range(magic_string.i):
        res += "BestSchool"
        if x != (magic_string.i - 1):
            res += ", "

    return(res)
