#!/bin/bash
# displays all the HTTP methods a server will accept
curl -s -L -X OPTIONS "$1"
