#!/usr/bin/python3
""" defines a script that adds all arguments to a Python list,
    and then save them to a file """


import os.path
import sys
savej = __import__('5-save_to_json_file').save_to_json_file
loadj = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
mylist = []

if os.path.isfile(filename) == False:
    savej(mylist, filename)

mylist = loadj(filename)

for i in range(1, len(sys.argv)):
    mylist.append(sys.argv[i])

savej(mylist, filename)
