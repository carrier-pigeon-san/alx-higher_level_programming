#!/usr/bin/python3
"""Definition of a class `Square`, that defines a square"""


class Square:
    """
    Square class defines a square with a private attribute `size`,
    that is a required integer greater than or equal to zero
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        a, b = value
        if type(a) is not int or type(b) is not int:
            raise TypeError('position must be a tuple of 2 positive integers')
        if a < 0 or b < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
        else:
            for o in range(self.__position[1]):
                print()
            for m in range(self.__size):
                for p in range(self.__position[0]):
                    print(" ", end="")
                for n in range(self.__size):
                    print("#", end="")
                print()

    def __repr__(self):
        if self.__size == 0:
            return "\n".join([])
        nest = [[] if (i < self.__position[1]) else
                [
                    " " if (j < self.__position[0]) else "#"
                    for j in range(self.__size + self.__position[0])
                    ]
                for i in range(self.__size + self.__position[1])
                ]
        return "\n".join([''.join(i) for i in nest])
