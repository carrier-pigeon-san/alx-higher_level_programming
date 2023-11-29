#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        print("{} is lower".format(c))
    elif ord(c) >= 65 and ord(c) <= 90:
        print("{} is upper".format(c))
