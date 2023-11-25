#!/usr/bin/python3

"""
    This script contains a function to add 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Parameters:
        a (int): first integer.
        b (int): second integer. Defualt is 98

    Returns:
        int: the addition of a and b

    Raises:
        TypeError: if the provided values are not an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + (b)
