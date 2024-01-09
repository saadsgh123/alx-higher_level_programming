#!/usr/bin/python3
# 0-read_file.py
# saadsgh123 <sdsghouri@gmail.com>

def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
