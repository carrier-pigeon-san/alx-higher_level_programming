#!/usr/bin/python3
"""Definition of a class `Square`, that defines a square"""


class Square:
    """
    Square class defines a square with a private attribute `size`,
    that is a required integer greater than or equal to zero
    """

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return self.__size ** 2
