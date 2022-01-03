#!/usr/bin/python3
def no_c(my_string):
    count:int = 0
    for char in my_string:
        print(char)
        if (char == 'c' or char == 'C'):
            my_string = my_string[:count] + my_string[count + 1:]
            continue
        count += 1

    return (my_string)
