#!/usr/bin/python3
""" Defines a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a class Rectangle that inherits
        from BaseGeometry (7-base_geometry.py).
         (task based on 8-rectangle.py)
        Args:
            width (int): parameter of type int.
            height (int): parameter of type int.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return calc value of area."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
