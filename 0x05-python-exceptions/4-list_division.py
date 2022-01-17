#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_res = []
    for i in range(list_length):
        try:
            res = (my_list_1[i] / my_list_2[i])
        except Exception as ex:
            err = type(ex).__name__
            if (err == "IndexError"):
                print("out of range")
            if (err == "ZeroDivisionError"):
                print("division by 0")
            if (err == "TypeError"):
                print("wrong type")

            res = 0
        finally:
            list_res.append(res)

    return(list_res)
