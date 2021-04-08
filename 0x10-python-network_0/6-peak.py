#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """

def find_peak(list_of_integers):
    """ def func """
    if len(list_of_integers) == 0:
        return (None)
    a = list_of_integers[1]
    for i in range(2 , (len(list_of_integers))):
        if list_of_integers[i] > a:
            a = list_of_integers[i]
    return (a)
