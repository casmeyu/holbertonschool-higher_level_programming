#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return[i**2 for i in list(map((lambda x: x), matrix))]
