#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if type(first_name) == str:
        if type(last_name) == str:
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
