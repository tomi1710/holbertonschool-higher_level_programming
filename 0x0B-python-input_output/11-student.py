#!/usr/bin/python3
""" defines a class Student that defines a student
    by: (based on 10-student.py) """


class Student:
    """ class Student """
    def __init__(self, first_name, last_name, age):
        """ def """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ def """
        new = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    new[i] = self.__dict__[i]
            return new

    def reload_from_json(self, json):
        """ def """
        for i in json:
            if i in self.__dict__:
                self.__dict__[i] = json[i]
