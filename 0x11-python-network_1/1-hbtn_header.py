#!/usr/bin/python3
"""This module contains a python script that takes in a URL, sends a request
to the URL and displays the value of the `X-Request-id` variable found in the
header of the response"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == '__main__':
    link = argv[1]
    http = Request(link)

    with urlopen(http) as response:
        header = response.info()

    print(header.get('X-Request-Id'))
