#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
    displays the body of the response """
import request
from sys import argv

if __name__ == '__main__':
    res = request.get(argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
