#!/usr/bin/python3
import json
""" functions a function that creates an Object from a JSON file """


def load_from_json_file(filename):
    """ function """
    with open(filename) as f:
        return json.load(f)
