#!/usr/bin/python3
"""
    0-add_integer: add_integer()
"""


def add_integer(a, b=98):
    """
        add_integer returns the sum of two integers
        Args:
            a: first number.
            b: second number.
        Returns:
            sum of the two integers
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
