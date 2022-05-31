#!/usr/bin/python3
import random
number = random.randint(-10,10)
n = int(input("enter the number:"))
if n > 0:
    print(n, "is a positive number")
elif n == 0:
    print(n, "is a zero number")
else:
    print(n, "is a negative number" )
