#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
    moss = [[1]]
    while len(moss) != n:
        mos = moss[-1]
        mok = [1]
        for j in range(len(mos) - 1):
            mok.append(mos[j] + mos[j + 1])
        mok.append(1)
        moss.append(mok)
    return moss
