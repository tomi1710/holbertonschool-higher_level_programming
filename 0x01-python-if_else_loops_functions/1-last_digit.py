#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = str(number)
    number1 = int(number[0] + number[-1])
else:
    number = str(number)
    number1 = int(number[-1])
if number1 > 5:
    print("Last digit of {} is {:d} and is greater than 5". format(number, number1))
elif number1 == 0:
    print("Last digit of {} is 0 and is 0". format(number))
else:
    print("Last digit of {} is {:d} and is less than 6 and not 0". format(number, number1))
