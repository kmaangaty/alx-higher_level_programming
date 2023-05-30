#!/usr/bin/python3
""" Square class Define"""


class Square:
    """square represented"""
    def __init__(self, size=0):
        """Initialize a new class.
        Args: size (int): parameter of type int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
