#!/usr/bin/python3
""" rectangle class """


class Rectangle:
    """ class rectangle """
    def __init__(self, width=0, height=0):
        """ iniciar """
        self.height = height
        self.width = width

    def __str__(self):
        """ returns """
        rep = ""
        if not self.area():
            return (rep)
        for row in range(self.height):
            rep = rep + "#" * self.width
            if row != self.height - 1:
                rep = rep + "\n"
        return (rep)

    def __repr__(self):
        """ return a string """
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ delete """
        print("Bye rectangle...")

    @property
    def width(self):
        """ returns private width """
        return (self.__width)

    @width.setter
    def width(self, value):
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns area """
        return (self.width * self.height)

    def perimeter(self):
        """ returns perimeter """
        if self.area() is 0:
            return (0)
        return (2 * self.width) + (2 * self.height)
