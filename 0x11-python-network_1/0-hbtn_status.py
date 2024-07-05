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
print('    - type: {}'.format(type(content)))
print('    - content: {}'.format(content))
print('    - utf8 content: {}'.format(content.decode('utf-8')))
