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
    for char in range(len(text)):
        if text[char] in ('.', '?', ':'):
            print(char)
            print()
        elif text[char-1] in ('.', '?', ':') and text[char] == ' ':
            continue
        else:
            print('{:s}'.format(text[char]), end="")
