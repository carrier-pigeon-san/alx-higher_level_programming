#!/usr/bin/python3
"""
contains is_same_class() function that returns boolean based on whether a
given object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    is_same_class() returns 'True' if the object 'obj' is exactly an instance
    of the 'a_class'; otherwise 'False'
    """

    if type(obj) is a_class:
        return True
    else:
        return False
