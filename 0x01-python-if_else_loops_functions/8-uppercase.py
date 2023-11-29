#!/usr/bin/python3
def uppercase(s):
    new_str = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            new_str += chr(ord(char) - 32)
        elif char == " ":
            new_str += char
        else:
            new_str += char
    print("{}".format(new_str))
