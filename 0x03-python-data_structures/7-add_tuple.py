#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Addition of tuple_a and tuple_b
    Args:
        tuple_a: tuple a
        tuple_b: tuple b
    Returns:
        tuple a + b
    """
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    if len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    return (x, y)
