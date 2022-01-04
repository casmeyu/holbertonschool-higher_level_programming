#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    br = True
    if value:
        while br:
            for key in a_dictionary:
                if a_dictionary[key] == value:
                    a_dictionary.pop(key)
                    break
            br = False

    return (a_dictionary)
