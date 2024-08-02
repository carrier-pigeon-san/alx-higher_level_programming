#!/usr/bin/python3
"""This module contains a script that takes in a letter and sends a POST
request to `http://0.0.0.0:5000/search_user` with the letter as a parameter"""
from sys import argv
import requests
from requests import exceptions

if __name__ == '__main__':
    link = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ""
    r = requests.post(link, data={'q': q})
    try:
        j = r.json()
    except requests.exceptions.InvalidJSONError:
        print("Not a valid JSON")
    else:
        if j:
            print('[{}] {}'.format(j.get('id'), j.get('name')))
        else:
            print("No result")
