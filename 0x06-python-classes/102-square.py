#!/usr/bin/python3
""" Square class Define"""


class Square:
    """Square represented"""
    def __init__(self, size=0):
        """Initialize a new class.
        Args:
            size (int): parameter of type int.
        """
        self.size = size

    @property
    def size(self):
        """getter or setter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return (self.__size * self.__size)

    def __eq__(self, other):
        """define calc value by ==."""
        return self.area() == other.area()

    def __ne__(self, other):
        """define calc value by !=."""
        return self.area() != other.area()

    def __lt__(self, other):
        """define calc value by <."""
        return self.area() < other.area()

    def __le__(self, other):
        """define calc value by <=."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """define calc value by >."""
        return self.area() > other.area()

    def __ge__(self, other):
        """define calc value by >=."""
        return self.area() >= other.area()
