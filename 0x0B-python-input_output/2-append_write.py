#!/usr/bin/python3
""" defines a function that appends a string at the end of a text
     file (UTF8) and returns the number of characters added """


def append_write(filename="", text=""):
    """ function """
    with open(filename, "a") as f:
        f.write(text)

    return(len(text))
