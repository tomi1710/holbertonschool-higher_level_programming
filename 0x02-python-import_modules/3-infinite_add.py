#!/usr/bin/python3
import sys
argc = len(sys.argv) - 1
suma = 0
if argc == 0:
    print("0")
else:
    for i in range(1, argc + 1):
        suma = suma + int(sys.argv[i])
    print("{:d}".format(suma))
