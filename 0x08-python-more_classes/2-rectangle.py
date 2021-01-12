#!/usr/bin/python3
""" define a class rectangle """


class Rectangle:
    """ rectangle class """

    def __init__(self, width=0, height=0):
        """ self """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width class """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height class """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ heigth setter """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area """
        return (self.width * self.height)

    def perimeter(self):
        """ returns the perimeter """
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * self.width) + (2 * self.height)
