#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) == float or type(a) == int:
        if type(b) == float or type(b) == int:
            return (a + b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")
