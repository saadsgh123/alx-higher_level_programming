#!/usr/bin/python3
def print_last_digit(number):
    last = 0
    if number < 0:
        number = abs(number)
    last = number % 10
    print("{}".format(l), end="")
    return last
