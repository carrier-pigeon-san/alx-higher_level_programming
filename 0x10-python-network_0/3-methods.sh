#!/bin/bash
# displays all the HTTP methods a server will accept
curl -s -L -I "$1" | grep Allow
