#!/usr/bin/python3
"""definition of a class - Rectangle"""


class Rectangle:
    """a class that defines a Rectangle"""

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """computes and returns the area of a rectangle"""

        return self.__width * self.__height

    def perimeter(self):
        """computes and returns the perimeter of a rectangle"""

        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return '\n'.join([])
        rect = [
                [
                    "#" for j in range(self.__width)
                    ]
                for i in range(self.__height)
                ]
        return '\n'.join([''.join(i) for i in rect])

    def __repr__(self):
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
