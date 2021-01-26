#!/usr/bin/python3
""" defines a class Rectangle """
from models.base import Base
import sys
import json
import csv


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
        """ def """
        return self.__width

    @width.setter
    def width(self, value):
        """ def """
        self.intvalidator("width", value)
        self.__width = value

    @property
    def height(self):
        """ def """
        return self.__height

    @height.setter
    def height(self, value):
        """ def """
        self.intvalidator("height", value)
        self.__height = value

    @property
    def x(self):
        """ def """
        return self.__x

    @x.setter
    def x(self, value):
        """ def """
        self.intvalidator("x", value)
        self.__x = value

    @property
    def y(self):
        """ def """
        return self.__y

    @y.setter
    def y(self, value):
        """ def """
        self.intvalidator("y", value)
        self.__y = value

    def area(self):
        """ def """
        return (self.__width * self.__height)

    def __str__(self):
        """ def """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def display(self):
        """ def """
        for a in range(self.__y):
            print("")
        for c in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for d in range(self.__width - 1):
                print("#", end="")
            print("#")

    def update(self, *args, **kwargs):
        """ def """
        if args and (len(args) > 0):
            if len(args) > 1:
                self.intvalidator("width", args[1])
                self.__width = args[1]
            if len(args) > 2:
                self.intvalidator("height", args[2])
                self.__height = args[2]
            if len(args) > 3:
                self.intvalidator("x", args[3])
                self.__x = args[3]
            if len(args) > 4:
                self.intvalidator("y", args[4])
                self.__y = args[4]
            if len(args) > 0:
                self.id = args[0]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.__width = val
                elif key == "height":
                    self.__height = val
                elif key == "x":
                    self.__x = val
                elif key == "y":
                    self.__y = val

    def to_dictionary(self):
        """ def """
        return {"x": self.__x, "y": self.__y, "id": self.id,
                "width": self.__width, "height": self.__height}
