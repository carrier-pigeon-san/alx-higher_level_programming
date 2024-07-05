#!/usr/bin/python3
"""This module contains a script that takes in a URL and an email address,
sends a POST request to the URL with the email as a parameter, and displays
the body of the response"""
from sys import argv
import requests

if __name__ == '__main__':
    link = argv[1]
    param = {'email': argv[2]}
    r = requests.post(link, param)
    print(r.text)
