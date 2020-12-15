#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)

    mx = -10000
    for i in range(len(my_list)):
        if (my_list[i] > mx):
            mx = my_list[i]
    return (mx)
