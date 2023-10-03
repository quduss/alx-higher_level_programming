#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 0:
        x = i + 65
    elif i % 2 == 1:
        x = i + 97
    print("{}".format(chr(x)), end='')
