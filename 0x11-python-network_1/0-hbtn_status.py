#!/usr/bin/python3
"""
This module is a python script that utilizes `urllib` package to fetch the url
`https://alx-intranet.hbtn.io/status`
"""
from urllib.request import Request, urlopen
link = "https://alx-intranet.hbtn.io/status"
http = Request(link)
with urlopen(http) as response:
    content = response.read()

print('Body response:')
print('\t- type: {}'.format(type(content)))
print('\t- content: {}'.format(content))
print('\t- utf8 content: {}'.format(content.decode('utf-8')))
