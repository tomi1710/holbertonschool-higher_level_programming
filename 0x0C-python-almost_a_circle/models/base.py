#!/usr/bin/python3
""" defines a class base """


class Base:
    """ class Base """
    __nb_objects = 0
    def __init__(self, id=None):
        """ def """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def intvalidator(self, name, value):
        """ def """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))
        elif value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))
