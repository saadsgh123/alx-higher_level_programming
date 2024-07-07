#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
"""
import urllib.request
import sys
import urllib.error


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
