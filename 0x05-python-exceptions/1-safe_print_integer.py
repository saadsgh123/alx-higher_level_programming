#!/usr/bin/python3
def safe_print_integer(value):
    try:
        new = int(value)
        print("{:d}".format(new))
        return True
    except ValueError:
        return False
