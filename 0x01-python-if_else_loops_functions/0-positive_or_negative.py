#!/usr/bin/python3
import random
number = random.randint(-10,10)
if number>0:
    print(number, "is a positive number")
elif number== 0:
    print(number, "is a zero number")
else:
    print(number, "is a negative number" )
