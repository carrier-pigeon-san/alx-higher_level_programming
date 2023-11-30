#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print(f"1: {argv[1]}")
    else:
        print(f"{len(argv) - 1:d} arguments:")
        for i in range(len(argv)):
            if i > 0:
                print("{}: {}".format(i, argv[i]))
