#!/usr/bin/python3
def uniq_add(my_list=[]):
    u_list = set(my_list)
    res = 0
    for n in u_list:
        res += n

    return (res)
