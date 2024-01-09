#!/usr/bin/python3
"""
inherits_from() determines whether object is an instance of the subclass of a
given superclass
"""


def inherits_from(obj, a_class):
    """
    returns True if object is an instance of a subclass of a given superclass
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
