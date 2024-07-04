#!/bin/bash
# The script accepts a URL, to which it sends a DELETE request, and displays the body of the response
curl -sX DELETE "$1"
