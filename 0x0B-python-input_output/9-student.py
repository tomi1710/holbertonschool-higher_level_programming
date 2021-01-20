#!/usr/bin/python3
""" defines a class Student that defines a student """


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ def """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ def dict """
        return self.__dict__
