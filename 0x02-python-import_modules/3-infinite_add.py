#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum_args = 0
    if len(argv) == 1:
        print(0)
    else:
        for i in range(len(argv)):
            if i >= 1:
                sum_args = sum_args + int(argv[i])
        print(f"{sum_args}")
