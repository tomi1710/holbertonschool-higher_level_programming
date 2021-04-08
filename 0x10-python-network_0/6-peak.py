#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ def func """
    if len(list_of_integers) == 0:
        return (None)
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    if len(list_of_integers) == 2:
        return (max(list_of_integers))
    a = list_of_integers[1]
    for i in range(2, (len(list_of_integers) - 1)):
        if list_of_integers[i] > a:
            a = list_of_integers[i]
    return (a)
