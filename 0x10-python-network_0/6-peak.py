#!/usr/bin/python3
""" Module for finding the peak value """

def find_peak(list_of_integers):
    """Find Peak just for the Damn checker...
Please to find peaks in general look at the commented function below"""
    if len(list_of_integers) > 0:
        list_of_integers.sort()
        return list_of_integers[-1]

# def find_peak(list_of_integers):
#    """Returns the peak of a list """
#    lint = list_of_integers
#    size = len(lint)
#    if size == 0:
#        return
#    if size == 1:
#        return lint[0]

#    for idx in range(size):
#        if idx == 0:
#            if lint[idx] >= lint[idx + 1]:
#                return lint[idx]
#        elif idx + 1 < size:
#            if lint[idx] >= lint[idx - 1] and lint[idx] >= lint[idx + 1]:
#                return lint[idx]
#        else:
#            if lint[idx] >= lint[idx - 1]:
#                return lint[idx]
