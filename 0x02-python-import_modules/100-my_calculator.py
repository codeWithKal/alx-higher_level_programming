#!/usr/bin/python3


from email import message


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    var = sys.argv
    le = len(var) - 1
    if le != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(var[1])
        b = int(var[3])
        c = var[2]
        if c == '+':
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif c == '-':
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif c == '*':
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        elif c == '/':
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
