#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = number % 10
last digit = number % 10
if number > 5:
    print("Last digit of {} is {} and is greater than 5" .format("number", "last digit"))
elif number == 0:
    print("Last digit of {} is and is 0" .format("number", "last digit"))
else:
    print("Last digit of  and is less than 6 and not 0" .format("number", "last digit"))
