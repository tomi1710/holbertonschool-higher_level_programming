#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
    displays the body of the response
    (decoded in utf-8)"""

import urllib.error as error
import urllib.request as call
from sys import argv

if __name__ == "__main__":
    datos = call.Request(argv[1])
    try:
        with call.urlopen(datos) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
