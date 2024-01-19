#!/usr/bin/python3
"""
load_from_json_file() function module
"""


import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as doc:
        return json.load(doc)
