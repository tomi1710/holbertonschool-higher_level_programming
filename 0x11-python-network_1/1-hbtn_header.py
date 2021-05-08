#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the
    header of the response """
import urllib.request as call
from sys import argv

if __name__ == "__main__":
    datos = call.Request(argv[1])
    with call.urlopen(datos) as f:
        print(f.headers.get('X-Request-Id'))
