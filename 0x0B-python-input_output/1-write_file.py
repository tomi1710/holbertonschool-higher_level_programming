#!/usr/bin/python3
""" defines a function that writes a string to a text file (UTF8)
    and returns the number of characters written """


def write_file(filename="", text=""):
    """ function """
    with open(filename, "w") as f:
        f.write(text)

    return(len(text))
