#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers """


def find_peak(listt):
    """ def func """
    if len(listt) == 0:
        return (None)
    if len(listt) == 1:
        return (listt[0])
    if len(listt) == 2:
        return (max(listt))
    half = int(len(listt) / 2)
    if listt[half - 1] < listt[half] > listt[half + 1]:
        return (listt[half])
    if listt[half] < listt[half + 1]:
        return (find_peak(listt[listt[half]:]))
    else:
        return (find_peak(listt[:listt[half + 1]]))
