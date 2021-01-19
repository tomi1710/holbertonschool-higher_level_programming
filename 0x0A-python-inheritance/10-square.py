#!/usr/bin/python3
""" class Square that inherits from Rectangle (9-rectangle.py) """


class BaseGeometry:
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


class Square(BaseGeometry):
    """ defines a class Square inherited from BaseGeometry """
    def __init__(self, size):
        """ init """
        self.__size = size
        BaseGeometry.integer_validator(self, size, self.__size)

    def area(self):
        """ returns the area of the square """
        return (self.__size * self.__size)

    def __str__(self):
        """ returns the dimensions of the square """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
