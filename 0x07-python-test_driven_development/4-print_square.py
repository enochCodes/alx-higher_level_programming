#!/usr/bin/python3
"""
    this module print the square
"""


def print_square(size):
    charactor = "#"
    """
        print the square fro the argument size
        args:
            size
        if size is not int reaise typeError
        if size is less than 0 reaise ValueError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    i = 1
    while (i <= size):
        print("{}".format(charactor*size))
        i += 1
