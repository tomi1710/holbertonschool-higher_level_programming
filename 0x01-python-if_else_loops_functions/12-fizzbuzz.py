#!/usr/bin/python3
def fizzbuzz():
    for i in range(101):
        if 0 < i:
            if i % 5 == 0 and i % 3 == 0:
                print("FizzBuzz", end=" ")
            elif i % 5 == 0:
                print("Buzz", end=" ")
            elif i % 3 == 0:
                print("Fizz", end=" ")
            else:
                print("{:d}".format(i), end=" ")
