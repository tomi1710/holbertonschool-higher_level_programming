#!/usr/bin/python3
import json
""" defines a function that returns the JSON representation of an object
    (string) """


def to_json_string(my_obj):
    """ def """
    return json.dumps(my_obj)
