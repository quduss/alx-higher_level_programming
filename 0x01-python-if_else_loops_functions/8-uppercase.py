#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            x = ord(c) - 32
        else:
            x = ord(c)
        print("{}".format(chr(x)), end='')
    print("")
