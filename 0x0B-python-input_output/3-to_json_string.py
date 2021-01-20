#!/usr/bin/python3
""" defines a function that returns the JSON representation of an object
    (string) """
import json


def to_json_string(my_obj):
    """ def """
    return json.dumps(my_obj)
