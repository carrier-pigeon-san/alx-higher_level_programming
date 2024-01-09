#!/usr/bin/python3
"""
contains is_kind_of_class() function that determines inheritance of a given
object from specified class
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class() returns 'True' if the object 'obj' is an instance of/
    instance of a class inherited from; otherwise 'False'
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
