#!/usr/bin/python3
"""
save_to_json_file() function module
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file , using JSON representation"""

    with open(filename, 'w') as doc:
        json.dump(my_obj, doc)
