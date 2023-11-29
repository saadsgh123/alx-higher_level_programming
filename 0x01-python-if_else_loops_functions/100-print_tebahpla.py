#!/usr/bin/python3
def fizzbuzz():
    new = ""
    for char in range(ord('z'), ord('a') - 1, -1):
        if char % 2 == 0:
            new += "{}".format(chr(char))
        else:
            char = char - 32
            new += "{}".format(chr(char))
    print("{}".format(new), end="")

if __name__ == '__main__':
    fizzbuzz()
