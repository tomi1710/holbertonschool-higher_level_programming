#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry (7-base_geometry.py) """


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


class Rectangle(BaseGeometry):
    """ defines a class Rectangle inherited from BaseGeometry """
    def __init__(self, width, height):
        """ init """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, self.__width)
        BaseGeometry.integer_validator(self, height, self.__height)

    def area(self):
        """ returns the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ returns the dimensions of the rectangle """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
