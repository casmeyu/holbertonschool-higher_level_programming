#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    idx = 1
    if (not roman_string or type(roman_string) != str):
        return (0)
    if (len(roman_string) == 1):
        return (romans[roman_string[0]])
    for idx in range(1, len(roman_string)):
        if romans[roman_string[idx - 1]] < romans[roman_string[idx]]:
            res += (romans[roman_string[idx - 1]] * -1)
        else:
            res += romans[roman_string[idx - 1]]

    res += romans[roman_string[idx]]

    return res

#XXI
#IV
#CXXIV
#XCIX
#LXXXIX
