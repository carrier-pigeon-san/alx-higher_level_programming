#!/usr/bin/python3
"""print_square() function module"""


def print_square(size):
    """
    prints a string representation of a square usin '#' character
    @size: dimensions of the square
    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for dimension1 in range(size):
        for dimension2 in range(size):
            print("#", end="")
        print()
