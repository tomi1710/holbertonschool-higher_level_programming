#!/usr/bin/python3
""" defines a class rectangle """


class Rectangle:
    """ rectangle class """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__"""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ defines an area """
        return self.__width * self.__height

    def perimeter(self):
        """ defines a perimeter """
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ converts to string """
        rect = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """ returns """
        return("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """ deletes """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
