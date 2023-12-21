#!/usr/bin/python3
"""Definition of a class `Square`, that defines a square"""


class Square:
    """
    Square class defines a square with a private attribute `size`,
    that is a required integer greater than or equal to zero
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, alt):
        if isinstance(alt, Square):
            if self.__size == alt.__size:
                return True
        return False

    def __ne__(self, alt):
        if isinstance(alt, Square):
            if self.__size != alt.__size:
                return True
        return False

    def __gt__(self, alt):
        return self.__size > alt.__size

    def __ge__(self, alt):
        if isinstance(alt, Square):
            if self.__size >= alt.__size:
                return True
        return False

    def __lt__(self, alt):
        return self.__size < alt.__size

    def __le__(self, alt):
        if isinstance(alt, Square):
            if self.__size <= alt.__size:
                return True
        return False
