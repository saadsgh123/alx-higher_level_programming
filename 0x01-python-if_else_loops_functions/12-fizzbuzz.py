#!/usr/bin/python3
def fizzbuzz():
    new = ""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            new += "FizzBuzz "
        elif i % 3 == 0:
            new += "Fizz "
        elif i % 5 == 0:
            new += "Buzz"
        else:
            new += "{} ".format(i)
    print(new, end = " ")
