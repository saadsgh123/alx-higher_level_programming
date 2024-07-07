#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import urllib.request
import urllib.parse


url = sys.argv[1]
values = {'email': sys.argv[2]}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))
