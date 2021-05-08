#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    url = request.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(url.text)))
    print("\t- content: {}".format(url.content.decode('utf-8')))
