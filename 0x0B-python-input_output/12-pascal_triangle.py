#!/usr/bin/python3
""" defines a function def pascal_triangle(n): that returns a list
    of lists of integers representing the Pascals triangle of n """


def pascal_triangle(n):
    """ def """
    mylist = []
    mylist2 = []
    mylist3 = []

    if n <= 0:
        return mylist
        
    mylist = [1]
    mylist3.append(mylist)
    for a in range(n - 1):
        for i in range(len(mylist) + 1):
            if ((i == 0) or (i == len(mylist))):
                mylist2.append(1)
            else:
                mylist2.append(mylist[i] + mylist[i - 1])
        mylist3.append(mylist2)
        mylist = mylist2
        mylist2 = []

    return mylist3
