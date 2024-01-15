#!/usr/bin/python3
"""print_square() function module"""


def print_square(size):
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for l in range(size):
        for w in range(size):
            print("#", end="")
        print()
