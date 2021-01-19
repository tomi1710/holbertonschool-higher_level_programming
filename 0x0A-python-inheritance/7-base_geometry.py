#!/usr/bin/python3
""" defines a class BaseGeometry """


class BaseGeometry():
    """ class BaseGeometry """
    def area(self):
        """ defines area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the integer passed """
        if (type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        elif (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
