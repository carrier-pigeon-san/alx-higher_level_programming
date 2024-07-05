#!/usr/bin/python3
"""This module contains a python script that takes in a URL, sends a request
to the URL, and displays the body of the response"""
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from sys import argv

if __name__ == '__main__':
    link = argv[1]
    http = Request(link)

    try:
        with urlopen(http) as response:
            content = response.read().decode('utf-8')
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
    else:
        print(content)
