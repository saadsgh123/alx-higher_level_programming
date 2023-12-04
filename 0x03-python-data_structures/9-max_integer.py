#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None  # Return None for an empty list

    max_value = my_list[0]
    for value in my_list[1:]:
        if value > max_value:
            max_value = value

    return max_value
