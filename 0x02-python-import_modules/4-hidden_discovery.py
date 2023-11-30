#!/usr/bin/python3
if __name__ == "__main__":
    module = __import__("hidden_4")
    for n in dir(module):
        if ord(n[0]) >= 97 and ord(n[0]) <= 122:
            print(n)
