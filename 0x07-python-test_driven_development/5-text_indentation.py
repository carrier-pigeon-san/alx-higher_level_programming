#!/usr/bin/python3
"""
text_indentation() function module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these three characters:
    ',', '?' and ':'
    """

    if type(text) is not str:
        raise TypeError('text must be a string')
    for chars in '.:?':
        text = (chars + '\n\n').join(
                [substr.strip(" ") for substr in text.split(chars)])
    print(text, end="")
