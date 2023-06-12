#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Defines class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

    def __init__(self, width, height):
        """ Instantiation with width and height: def __init__(self, width, height):
            width and height must be private. No getter or setter
            width and height must be positive integers, validated by integer_validator
        Args:
            width (int): parameter of type int.
            height (int): parameter of type int.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
