#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ''
    for i in range(0, len(str)):
        if i == n:
            continue
        str_copy += str[i]
    return str_copy
