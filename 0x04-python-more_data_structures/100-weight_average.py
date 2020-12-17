#!/usr/bin/python3
def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)

    fsum = 0
    lsum = 0
    for i in range(len(my_list)):
        fsum = fsum + (my_list[i][0] * my_list[i][1])
    for i in range(len(my_list)):
        lsum = lsum + my_list[i][1]

    return (fsum / lsum)
