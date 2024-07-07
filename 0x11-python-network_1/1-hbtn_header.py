#!/usr/bin/python3
# Sends a request to the URL and displays the value of the X-Request-Id
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    print(dict(response.headers).get('X-Request-Id'))
