#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response.
Usage: ./6-post_email.py <URL>
  - Displays the status of the response.
"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.text)
    else:
        print(response.text)
