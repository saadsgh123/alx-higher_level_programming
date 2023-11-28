#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
newLast = 0
if number < 0:
    newLast = last * -1
else:
    newLast = last
if last > 5 or last == 5:
    print(f'Last digit of{number} is {newLast} and is greater than 5')
elif last > 6 and last != 0:
    print(f'Last digit of{number} is {newLast} is less than 6 and not 0')
elif last == 0:
    print("Last digit of {0} is {1} and is 0".format(number, last))
