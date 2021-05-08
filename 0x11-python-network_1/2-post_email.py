#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8) """

import urllib.parse as parse
import urllib.request as response
from sys import argv

if __name__ == "__main__":
    dict = {'email': argv[2]}
    elemento = parse.urlencode(dict).encode('utf-8')
    data = response.Request(argv[1], elemento)
    with response.urlopen(data) as res:
        print(res.read().decode('utf-8'))
