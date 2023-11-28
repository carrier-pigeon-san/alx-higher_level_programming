#!/usr/bin/python3
import random
number = random.randint(-19, 10)
if number != 0:
    if number > 0:
        print(f"{number:d} is positive")
    else:
        print(f"{number:d} is negative")
else:
    print(f"{number:d} is zero")
