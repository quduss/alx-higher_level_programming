#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for c in range(x):
        try:
            print(my_list[c], end='')
        except IndexError:
            print()
            return c
    print()
    return x
