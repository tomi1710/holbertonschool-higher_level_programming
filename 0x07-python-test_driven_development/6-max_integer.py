#!/usr/bin/python3
"""max integer function rellenar espacio jejeje
"""


def max_integer(list=[]):
    """this function searching the biggest number in a list if
    list have size 0 return none if not, the function return max integer
    """
    if len(list) != 0:
        biggest = list[0]
        i = 1
        for i in range(0, len(list)):
            if list[i] > biggest:
                biggest = list[i]
            i = i + 1
        return (biggest)
    else:
        return (None)
