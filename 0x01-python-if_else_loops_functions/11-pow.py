#!/usr/bin/python3
def pow(a, b):
    result = a
    for i in range(1, b):
        result *= a
    return result
