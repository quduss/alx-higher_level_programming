#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_ = len(sys.argv) - 1
    if len_ == 0:
        print("0 arguments.")
    elif len_ == 1:
        print("1 argument:")
    elif len_ > 1:
        print("{} arguments:".format(len_))
    for x in range(1, len_ + 1):
        print("{}: {}".format(x, sys.argv[x]))
