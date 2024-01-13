#!/usr/bin/python3
"""
module contains class 'Square' that exhibits properties of a square polygon
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class 'Square', superclass 'Rectangle', instantiated with private
    attribute, 'size' - a positive integer, greater than zero (0)
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """returns the area of a square"""

        return self.__size**2

    def __str__(self):
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
