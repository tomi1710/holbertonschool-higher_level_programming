#!/usr/bin/python3
""" defines a class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ def """
        self.intvalidator("width", width)
        self.__width = width
        self.intvalidator("height", height)
        self.__height = height
        self.intvalidator("x", x)
        self.__x = x
        self.intvalidator("y", y)
        self.__y = y
        self.id = id
        super(Rectangle, self).__init__(id)

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        self.intvalidator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        self.intvalidator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.x

    @x.setter
    def x(self, value):
        self.intvalidator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.y

    @y.setter
    def y(self, value):
        self.intvalidator("y", value)
        self.__y = value

    def area(self):
        """ def """
        return (self.__width * self.__height)

    def display(self):
        """ def """
        for i in range(self.__height):
            for a in range(self.__width - 1):
                print("#", end = "")
            print("#")

    def __str__(self):
        """ def """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
        self.__y, self.__width, self.__height)
