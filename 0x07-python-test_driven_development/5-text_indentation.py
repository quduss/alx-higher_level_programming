#!/usr/bin/python3

"""text indentation definition"""


def text_indentation(text):
    """function that prints a string
    but prints two lines after the dot, question mark
    and column characters in the string
    Args:
        text: string input
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    curr_idx = 0
    letters = ['.', '?', ':']
    len_ = len(text)
    while curr_idx < len_ and text[curr_idx] == ' ':
        curr_idx += 1

    while curr_idx < len_:
        print(text[curr_idx], end="")
        if text[curr_idx] in letters or text[curr_idx] == '\n':
            if text[curr_idx] in letters:
                print("\n")
            curr_idx += 1
            while curr_idx < len_ and text[curr_idx] == ' ':
                curr_idx += 1

            continue
        curr_idx += 1
