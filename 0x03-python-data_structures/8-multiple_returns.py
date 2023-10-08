#!/usr/bin/python3

def multiple_returns(sentence):
    """get length and first character of sentence
    Args:
        sentence: string input
    Returns:
        tuple of length and first character
    """
    length = len(sentence)
    if length == 0:
        first = None
    else:
        first = sentence[0]
    return (length, first)
