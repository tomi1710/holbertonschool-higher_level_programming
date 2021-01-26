#!/usr/bin/python3
""" defines a class base """
import sys
import json


class Base:
    """ class Base """
    __nb_objects = 0
    def __init__(self, id=None):
        """ def """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def intvalidator(self, name, value):
        """ def """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0 and (name == "x" or name == "y"):
            raise ValueError("{} must be >= 0".format(name))
        elif value <= 0 and (name == "width" or name == "height"):
            raise ValueError("{} must be > 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """ def """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation of list_objs to a file"""
        listo = []
        filename = cls.__name__ + ".json"
        if list_objs is not None:
            with open(filename, 'w') as f:
                for a in list_objs:
                    listo.append(cls.to_dictionary(a))
                f.write(Base.to_json_string(listo))
        else:
            with open(filename, 'w') as f:
                f.write(listo)

    @staticmethod
    def from_json_string(json_string):
        """ def """
        lista = []
        if json_string is not None and json_string:
            return json.loads(json_string)
        else:
            return lista

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if (cls.__name__ == "Square"):
            a = cls(1)
        elif (cls.__name__ == "Rectangle"):
            a = cls(1, 1)
        a.update(**dictionary)
        return a

    def load_from_file(cls):
        """ def """
