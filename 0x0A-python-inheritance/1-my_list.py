#!/usr/bin/python3
""" defines a class MyList """


class MyList(list):
    """ MyList class """
    def print_sorted(self):
        """ sorts by order """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
