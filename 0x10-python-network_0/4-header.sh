#!/bin/bash
# This script accepts a URL, to which a GET request is sent with a custom header variable
curl -s -H X-School-User-Id:98 "$1"
