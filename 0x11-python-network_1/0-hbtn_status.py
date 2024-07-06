#!/usr/bin/python3
# Python script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html = response.read()
    print(f"Body response:\n - type: {type(html)}\n - content: {html}\n"
          f" - content: {html.decode('utf-8')}")
