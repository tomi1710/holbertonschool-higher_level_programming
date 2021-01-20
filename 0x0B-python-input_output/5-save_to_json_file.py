#!/usr/bin/python3
import json
""" defines a function that writes an Object to a text file, using a
    JSON representation: """


def save_to_json_file(my_obj, filename):
    """ functions """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
