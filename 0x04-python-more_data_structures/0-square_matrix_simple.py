#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for i in range(len(matrix)):
        newmatrix.append(list(map((lambda a : a * a), matrix[i])))
    return (newmatrix)
