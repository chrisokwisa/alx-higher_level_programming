#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = number % 10
if number > 5:
    print("Last digit of 98 is 8 and is greater than 5")
elif number == 0:
    print("Last digit of 0 is 0 and is 0")
else:
    print("Last digit of -98 is -8 and is less than 6 not 0")
