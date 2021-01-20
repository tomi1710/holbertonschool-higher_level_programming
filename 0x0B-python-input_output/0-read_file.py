#!/usr/bin/python3
""" defines a function that reads a text file (UTF8) and prints
    it to stdout """


def read_file(filename=""):
    """ def """
    with open(filename) as f:
        for line in f:
            print(line, end="")
