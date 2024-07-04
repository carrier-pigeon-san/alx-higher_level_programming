#!/bin/bash
# This script accepts a URL, to which a POST request is sent with specific variables
curl -s -d email=test@gmail.com -d subject="I will always be here for PLD" "$1"
