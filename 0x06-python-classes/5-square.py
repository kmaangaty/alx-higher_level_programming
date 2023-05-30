#!/usr/bin/python3
""" Square class Define"""


class Square:
    """square represented"""
    def __init__(self, size):
        """Initialize a new class.
        Args: size (int): parameter of type int.
        """
        self.size = size

    @property
    def size(self):
        """set or get square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return calc value."""
        return (self.__size * self.__size)

    def my_print(self):
        """print square by # char"""
        for i in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
