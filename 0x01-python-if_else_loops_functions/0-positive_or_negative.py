#!/usr/bin/python3
import random
number = random.randint(-10,10)
if number > 0:
    print("%d is positive\n", number)
elif number == 0:
    print("%d is zero\n", number)
else:
    print("%d negative\n", number)
