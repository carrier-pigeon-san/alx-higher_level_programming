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

    def my_print(self):
        if self.__size == 0:
            print()
        for m in range(self.__size):
            for n in range(self.__size):
                if n < self.__size:
                    print("#", end="")
            print()
