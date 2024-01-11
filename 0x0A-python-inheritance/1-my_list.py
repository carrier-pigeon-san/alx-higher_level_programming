#!/usr/bin/python3
"""
class 'MyList', subclass of 'list'
"""


class MyList(list):
    """
    MyList subclass of 'list'
    """

    def __init__(self, a_list=[]):
        super().__init__(a_list)

    def print_sorted(self):
        """prints a sorted list of integers in ascending order"""

        self.sort()
        print(self)
