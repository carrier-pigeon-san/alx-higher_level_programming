#!/bin/bash
# The script accepts a URL, to which it sends a GET request, and displays the body of the response
curl -f -s -L "$1"
