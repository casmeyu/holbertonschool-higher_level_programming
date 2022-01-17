#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except Exception as ex:
            if (type(ex).__name__ == "ValueError"):
                continue
            else:
                break
    print()
    return(count)
