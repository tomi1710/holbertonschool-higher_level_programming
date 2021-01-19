#!/usr/bin/python3


def inherits_from(obj, a_class):
    """ checks if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class """
    if (a_class == type(obj)):
        return False
    else:
        return isinstance(obj, a_class)
