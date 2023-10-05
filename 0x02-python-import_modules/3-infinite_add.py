#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_ = len(sys.argv)
    sum = 0
    if len_ == 1:
        print("{}".format(sum))
    elif len_ > 1:
        for x in range(1, len_):
            sum += int(sys.argv[x])
        print("{}".format(sum))
