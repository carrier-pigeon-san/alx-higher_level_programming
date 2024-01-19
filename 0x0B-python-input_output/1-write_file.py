#!/usr/bin/python3
"""
write_file() function module
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF-8) and returns the number
    of characters written
    """

    with open(filename, 'w', encoding="utf-8") as doc:
        return doc.write(text)
