#!/usr/bin/python3
"""
add_attribute() function module for adding dynamically created attributes to a
class object
"""


def add_attribute(obj, name=None, attr=None):
    """adds a new attribute to object if possible"""

    if not issubclass(type(obj), object):
        raise TypeError('can\'t add new attribute')
    if not hasattr(obj, '__dict__'):
        raise TypeError('can\'t add new attribute')
    obj.name = attr
