#!/usr/bin/python3

def no_c(my_string):
    count = 0
    copy = my_string[:]

    for char in copy:
        if (char == 'c' or char == 'C'):
            copy = copy[:count] + copy[count + 1:]
            continue
        count += 1

    return (copy)
