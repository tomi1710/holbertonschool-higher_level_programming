#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    r = int(number[-1])
    print("{:d}".format(r), end="")
    return(r)
