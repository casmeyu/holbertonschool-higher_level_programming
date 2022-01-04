#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    max_key = ""

    if not a_dictionary:
        return (None)

    for item in a_dictionary:
        if a_dictionary[item] > max_score:
            max_score = a_dictionary[item]
            max_key = item

    return (max_key)
