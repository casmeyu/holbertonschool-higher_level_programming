#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except Exception as ex:
            errname = type(ex).__name__
            if (errname == "ValueError" or errname == "TypeError"):
                continue
            else:
                break
    print()
    return(count)
