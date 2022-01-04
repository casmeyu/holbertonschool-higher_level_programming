#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    br = True
    while br:
        for key in a_dictionary:
            if a_dictionary[key] == value:
                del a_dictionary[key]
                break
            else:
                br = False

    return (a_dictionary)
