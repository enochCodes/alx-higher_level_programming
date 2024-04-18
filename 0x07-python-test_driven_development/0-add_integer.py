#!/usr/bin/python3
"""
    a module to add two integers
"""
def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats,
    otherwise raise a TypeError exception
    Returns an integer: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
