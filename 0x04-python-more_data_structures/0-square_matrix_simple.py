#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for line in matrix:
        new_line = map((lambda x: x * x), line)
        new_matrix.append(list(new_line))

    return new_matrix
