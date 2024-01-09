#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """function that returns the list of available attributes and methods of an object
    Args:
        obj: object to check
    """
    return dir(obj)
