#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """
import urllib.request as call

if __name__ == "__main__":
    with call.urlopen('https://intranet.hbtn.io/status') as f:
        datos = f.read()
        print('Body response:')
        print("\t- type: {}".format(type(datos)))
        print("\t- content: {}".format(datos))
        print("\t- utf8 content: {}".format(datos.decode('utf-8')))
