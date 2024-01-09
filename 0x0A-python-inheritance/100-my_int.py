#!/usr/bin/python3
"""
module defines class MyInt
"""


class MyInt(int):
    """
    a rebel subclass of int class that responds to '==' and '!=' in an
    inverted way
    """

    def __init__(self, num):
        int.__init__(num)

    def __eq__(self, alt):
        if isinstance(alt, MyInt):
            if self == alt:
                return True
        else:
            return False

    def __ne__(self, alt):
        if isinstance(alt, MyInt):
            if self != alt:
                return False
        else:
            return True
