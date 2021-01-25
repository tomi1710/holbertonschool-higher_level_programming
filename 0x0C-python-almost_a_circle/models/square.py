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

    def update(self, *args, **kwargs):

        if args and len(args) > 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.intvalidator("width", args[1])
                self.__size = args[1]
            if len(args) > 2:
                self.intvalidator("x", args[2])
                self._Rectangle__x = args[2]
            if len(args) > 3:
                self.intvalidator("y", args[3])
                self._Rectangle__y = args[3]
        else:
            for key, val in kwargs.items():
                if key == "id":
                    self.id = val
                if key == "size":
                    self.intvalidator("width", val)
                    self.__size = val
                if key == "x":
                    self.intvalidator("x", val)
                    self._Rectangle__x = val
                if key == "y":
                    self.intvalidator("y", val)
                    self._Rectangle__y = val

    def to_dictionary(self):
        """ def """
        return {"x": self._Rectangle__x, "y": self._Rectangle__y,
        "id": self.id, "size": self.__size}
