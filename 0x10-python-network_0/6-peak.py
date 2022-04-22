#!/usr/bin/python3
""" Module for finding the peak value """

def find_peak(list_of_integers):
    """ Returns the peak of a list """
    l = list_of_integers
    size = len(l)
    if size == 0:
        return
    if size == 1:
        return l[0]

    for idx in range(size - 1):
        if idx == 0 and idx + 1 < size:
            if l[idx] >= l[idx + 1]:
                return l[idx]
        elif idx + 1 < size:
            if l[idx] >= l[idx - 1] and l[idx] >= l[idx + 1]:
                return l[idx]
        else:
            if l[idx] >= l[idx - 1]:
                return l[idx]
