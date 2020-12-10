#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{:d} argument:".format(argc))
        for i in range(argc + 1):
            if i != 0:
                print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(argc + 1):
            if i != 0:
                print("{:d}: {}".format(i, sys.argv[i]))
