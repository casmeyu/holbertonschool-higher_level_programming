#!/usr/bin/python3
""" Module for finding the peak value """


def find_peak(list_of_integers):
    """ Returns the peak of a list """
    lint = list_of_integers
    size = len(lint)
    if size == 0:
        return
    if size == 1:
        return lint[0]

    for idx in range(size):
        if idx == 0:
            if lint[idx] >= lint[idx + 1]:
                return lint[idx]
        elif lint[idx + 1]:
            if lint[idx] >= lint[idx - 1] and lint[idx] >= lint[idx + 1]:
                return lint[idx]
        else:
            if lint[idx] >= lint[idx - 1]:
                return lint[idx]
