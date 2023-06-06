#!/usr/bin/python3
"""Addition function
    Args:
        a (int, float): parameter of type int.
        b (int, float): parameter of type int.
    Raises:
        TypeError: a and b must be integers or floats.
    Returns an integer: the addition of a and b.
    """


def add_integer(a, b=98):
    """Addition function.
    Args:
        a (int, float): parameter of type int.
        b (int, float): parameter of type int.
    Raises:
        TypeError: a and b must be integers or floats.
    Returns an integer: the addition of a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
