#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """ checks if he object is an instance of, or if the object is an instance
        of a class that inherited from, the specified class """
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
