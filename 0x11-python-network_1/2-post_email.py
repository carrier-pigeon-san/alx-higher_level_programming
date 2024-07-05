#!/usr/bin/python3
"""This module contains a python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == '__main__':
    link = argv[1]
    var = {'email': argv[2]}

    data = urlencode(var)
    data = data.encode('ascii')

    http = Request(link, data)
    with urlopen(http) as response:
        content = response.read().decode('utf-8')

    print(content)
