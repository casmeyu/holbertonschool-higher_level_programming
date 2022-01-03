#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and not matrix[0]:
        print()
        pass

    for line in matrix:
        for i in range(len(line)):
            if i == len(line) - 1:
                print("{:d}".format(line[i]))
            else:
                print("{:d}".format(line[i]), end=' ')
