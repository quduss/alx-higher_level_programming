#!/usr/bin/python3
for x in range(0, 8):
    for y in range(0, 10):
        if y > x:
            print("{:02d}, ".format(x * 10 + y), end='')
print("{}".format(89))
