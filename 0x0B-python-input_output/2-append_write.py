#!/usr/bin/python3
"""
append_write() function module
"""


def append_write(filename="", text=""):
    """
    append_write - appends a string at the end of a text file (UTF-8) and
    returns the number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as doc:
        return doc.write(text)
