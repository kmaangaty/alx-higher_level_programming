#!/usr/bin/python3
"""Defines a class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """Represent a class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """Public instance method: def area(self):
        that raises an Exception with the message area() is not implemented
        Public instance method: def integer_validator(self, name, value):
        that validates value:you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError
         exception with the message <name> must be greater than 0"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): parameter of type str.
            value (int): parameter of type int.
        Raises:
            if value is not an integer:
            raise a TypeError exception,
            with the message <name> must be an integer
            if value is less or equal to 0:
            raise a ValueError exception
            with the message <name> must be greater than 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
