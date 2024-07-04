#!/bin/bash
# The script accepts a URL, to which it sends a request , and displays the size of the body of the response in bytes
curl -sI "$1" | grep Content-Length | sed 's/Content-Length: //g'
