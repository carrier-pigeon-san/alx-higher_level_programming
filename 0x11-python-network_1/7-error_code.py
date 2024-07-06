#!/usr/bin/python3
"""This module contains a script that takes in a URL, sends a request to the
URL and displays the body of the response"""
from sys import argv
import requests

if __name__ == '__main__':
    link = argv[1]
    r = requests.get(link)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
