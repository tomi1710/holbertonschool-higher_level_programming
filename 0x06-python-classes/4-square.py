#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """__init__"""
        self.__size = size

    @property
    def size(self):
        """size"""
        return self.__size

    @size.setter
    def size(self, value):
        """size with value"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >=0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """area"""
        return self.__size * self.__size
