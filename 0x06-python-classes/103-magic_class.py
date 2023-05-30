#!/usr/bin/python3

""" MagicClass class Define"""

import math


class MagicClass:
    """MagicClass represented"""

    def __init__(self, radius=0):
        """Initialize a new class.
        Args:
            radius (float or int): parameter of type float or int.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return calc value."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return calc value."""
        return (2 * math.pi * self.__radius)
