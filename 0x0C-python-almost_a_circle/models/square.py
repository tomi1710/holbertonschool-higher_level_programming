#!/usr/bin/python3
""" Write the class Square that inherits from Rectangle """
from models.rectangle import Rectangle
from models.base import Base
import sys


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ def """
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self):
        """ def """
        return self.__size

    @size.setter
    def size(self, value):
        """ def """
        self.intvalidator("width", value)
        self.__size = value

    def __str__(self):
        """ def """
        return "[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x,
                                                self._Rectangle__y, self.__size)
