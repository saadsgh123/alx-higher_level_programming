#!/usr/bin/python3
# 5-save_to_json_file.py
# saadsgh123 <sdsghouri@gmail.com>
"""Defines a JSON file-writing function."""
import json



def save_to_json_file(my_obj, filename):
    """Write a function that writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as f:
        json_str = json.dumps(my_obj)
        return f.write(json_str)
