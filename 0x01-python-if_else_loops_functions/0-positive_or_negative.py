#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("is a positive number.")
elif number == 0:
    print("is a zero number.")
else:
    print("is a negative number." )
