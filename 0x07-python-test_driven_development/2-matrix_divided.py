#!/usr/bin/python3
def matrix_divided(matrix, div):

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (matrix is None):
        raise TypeError("matrix must be a matrix (list \
of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    new_list = []

    len_first_set = len(matrix[0])

    for row in range(len(matrix)):
        if len(matrix[row]) != len_first_set:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        new_list += [[float("{:.2f}".format(x / div)) for x in row]]

    return(new_list)
