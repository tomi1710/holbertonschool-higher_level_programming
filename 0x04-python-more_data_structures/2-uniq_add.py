#!/usr/bin/python3
def uniq_add(my_list=[]):
    lis = []
    ad = 0

    for i in range(len(my_list)):
        if my_list[i] not in lis:
            lis.append(my_list[i])

    for i in range(len(lis)):
        ad = ad + lis[i]

    return (ad)
