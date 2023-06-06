#!/usr/bin/python3
"""Print a square by specific char [#].
Args:
    size (int): parameter of type int.
Raises:
    TypeError: size must be an integer.
    ValueError: size must be >= 0.
"""


def print_square(size):
    """Print a square by specific char [#].
    Args:
        size (int): parameter of type int.
    Raises:
        TypeError: size must be an integer.
        ValueError: size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        [print("#", end="") for d in range(size)]
        print("")
