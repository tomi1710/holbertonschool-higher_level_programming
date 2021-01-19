#!/usr/bin/python3
""" class Rectangle that inherits from BaseGeometry (7-base_geometry.py) """
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """ defines a class Rectangle inherited from BaseGeometry """
    def __init__(self, width, height):
        """ init """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, self.__width)
        BaseGeometry.integer_validator(self, height, self.__height)
