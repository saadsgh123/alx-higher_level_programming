#!/usr/bin/python3
# 7-save_to_json_file.py
# saadsgh123 <sdsghouri@gmail.com>
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
