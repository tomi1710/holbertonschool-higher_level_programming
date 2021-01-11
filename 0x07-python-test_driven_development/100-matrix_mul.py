#!/usr/bin/python3

"""100-matrix_mul module
This module has only one function that calculates the product of two matrices
"""


def matrix_mul(m_a, m_b):
    """ matrix_mul(m_a, m_b)
    Function that multiplies two matrices. Each matrix should be a list of
    lists of integers or floats. Otherwise TypeError should be rised.
    If m_a or m_b is empty (it means: = [] or = [[]]): ValueError is raised.
    If m_a or m_b is not a rectangle (all rows should be of the same size)
    TypeError is raised. If m_a and m_b cant be multiplied: ValueError.
    Let m_a be of size "m x n" and m_b of size "n x p"
    """
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")

    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(li, list) for li in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(li, list) for li in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not all(type(n) in [int, float] for li in m_a for n in li):
        raise TypeError("m_a should contain only integers or floats")

    if not all(type(n) in [int, float] for li in m_b for n in li):
        raise TypeError("m_b should contain only integers or floats")

    row_l = len(m_a[0])
    if not all(len(m_a[i]) == row_l for i in range(len(m_a))):
        raise TypeError("each row of m_a must be of the same size")

    row_l = len(m_b[0])
    if not all(len(m_b[i]) == row_l for i in range(len(m_b))):
        raise TypeError("each row of m_b must be of the same size")

    n = len(m_a[0])
    if n != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m_c = []
    i = []
    res = 0
    for m in range(len(m_a)):
        i = []
        for p in range(len(m_b[0])):
            res = 0
            for k in range(n):
                res += (m_a[m][k] * m_b[k][p])
            i.append(res)
        m_c.append(i)

    return (m_c)
