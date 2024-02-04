#!/usr/bin/python3

""" This module add two integers"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): First integer to add
        b (int): Second integer to add

    Returns:
        int: The addition of a and b

    Raises:
        TypeError: Exception if a or b is not an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
