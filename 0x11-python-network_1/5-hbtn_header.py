#!/usr/bin/python3
"""This module contains a script that takes in a URL, sends a request to the
URL and displays the value of the variable `X-Request-Id in the response
header"""
from sys import argv
import requests

if __name__ == '__main__':
    link = argv[1]
    r = requests.get(link)
    print(r.headers.get('X-Request-Id'))
