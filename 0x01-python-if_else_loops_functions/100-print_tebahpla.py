#!/usr/bin/python3
i = 122
while i >= 97:
    zigzag = "even"
    if i % 2 != 0:
        i = i - 32
        zigzag = "odd"
    print("{:s}".format(chr(i)), end="")
    if zigzag == "odd":
        i = i + 32
    i = i - 1
