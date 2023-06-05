#!/usr/bin/python3
"""this file Define aclass name [Rectangle]"""


class Rectangle:
    """this is representation of Rectangle class"""

    def __init__(self, width=0, height=0):
        """Init a new object.

        Args:
            height (int): parameter of type int.
            width (int): parameter of type int.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter or setter for field width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter or setter for field height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
