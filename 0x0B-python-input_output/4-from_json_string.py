#!/usr/bin/python3
import json
""" defines a function that returns an object (Python data structure)
    represented by a JSON string """


def from_json_string(my_str):
    """ function """
    return json.loads(my_str)
