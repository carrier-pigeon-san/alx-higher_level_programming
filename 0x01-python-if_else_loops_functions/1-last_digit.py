#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number % 10 == 0:
    print(f"Last digit of {number} is {number % 10} and is 0")
else:
    print(f"Last digit of {number} is {number % 10} and not 0")
