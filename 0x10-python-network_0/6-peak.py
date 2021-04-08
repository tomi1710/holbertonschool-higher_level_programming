#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(listt):
    """ def func """
    if len(listt) == 0:
        return (None)
    elif len(listt) == 1:
        return (listt[0])
    elif len(listt) == 2:
        return (max(listt))
    half = int(len(listt) / 2)
    middle = listt[half]
    if listt[half - 1] < middle and middle > listt[half + 1]:
        return (middle)
    elif middle < listt[half + 1]:
        return (find_peak(listt[middle:]))
    else:
        return (find_peak(listt[:listt[half + 1]]))
