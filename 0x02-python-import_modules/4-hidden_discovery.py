#!/usr/bin/python3
import hidden_4


def printer():
    pt = dir(hidden_4)
    for i in pt:
        if i[:2] != '__':
            print("{:s}".format(i))


if __name__ == "__main__":
    printer()
