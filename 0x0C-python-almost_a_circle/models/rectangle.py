#!/usr/bin/python3
""" defines a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ def """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.id = id
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
