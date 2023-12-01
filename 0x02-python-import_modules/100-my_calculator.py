#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div

    length = len(sys.argv)

    if length >= 4:
        a = int(sys.argv[1])
        o = sys.argv[2]
        b = int(sys.argv[3])

        if o == '+':
            print("{} {} {} = {}".format(a, o, b, add(a, b)))
        elif o == '-':
            print("{} {} {} = {}".format(a, o, b, sub(a, b)))
        elif o == '/':
            print("{} {} {} = {}".format(a, o, b, div(a, b)))
        elif o == '*':
            print("{} {} {} = {}".format(a, o, b, mul(a, b)))
        else:
            print("Invalid operator. Supported operators are +, -, *, /")
            sys.exit(1)
    else:
        print("Usage: python script.py <operand1> <operator> <operand2>")
        sys.exit(1)
