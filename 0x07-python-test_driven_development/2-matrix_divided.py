#!/usr/bin/python3
"""Matrix divider
divides every item of a matrix by the div argument
"""


def matrix_divided(matrix, div):
    """divides items from a matrix by div
    Attributes:
        matrix ([[]]): matrix to divide
        div (int): divisor
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if (type(matrix) is list):
        line_len = len(matrix[0])
        for line in matrix:
            new_line = []
            if (type(line) is not list):
                raise TypeError(msg)
            if (len(line) != line_len):
                msg = "Each row of the matrix must have the same size"
                raise TypeError(msg)
            for item in line:
                if (type(item) is not int and type(item) is not float):
                    raise TypeError(msg)

                new_line.append(float("{0:.2f}".format((item/div))))

            new_matrix.append(new_line)
    else:
        raise TypeError(msg)

    return(new_matrix)
