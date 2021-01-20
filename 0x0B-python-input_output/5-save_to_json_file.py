#!/usr/bin/python3
""" defines a function that writes an Object to a text file, using a
    JSON representation: """
import json


def save_to_json_file(my_obj, filename):
    """ functions """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
