#!/bin/bash
# sends a request to a URL, and displays the size of the body of the responsee in bytes
curl -s "$1" | wc -c
