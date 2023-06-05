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

    @property
    def height(self):
        """getter or setter for field height"""
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the calculated value for field area in object."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the calculated value for field perimeter in object."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __repr__(self):
        """Return representation of the Rectangle."""
        shk = "Rectangle(" + str(self.__width)
        shk += ", " + str(self.__height) + ")"
        return shk

    def __del__(self):
        """Print a message "Bye rectangle..." for any object deletion"""
        print("Bye rectangle...")

    def __str__(self):
        """Return the printable representation"""
        if self.__width == 0 or self.__height == 0:
            return ""

        ash = []
        for z in range(self.__height):
            [ash.append('#') for x in range(self.__width)]
            if z != self.__height - 1:
                ash.append("\n")
        return "".join(ash)
