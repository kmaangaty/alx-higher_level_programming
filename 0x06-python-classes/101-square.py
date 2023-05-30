#!/usr/bin/python3
""" Square class Define"""


class Square:
    """Square represented"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new class.
        Args:
            size (int): parameter of type int.
            position (int): parameter of type int.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter or setter"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return calc value."""
        return (self.__size * self.__size)

    def my_print(self):
        """print calc value."""
        if self.__size == 0:
            print("")
            return

        [print("") for z in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            print("")

    def __str__(self):
        """stringify."""
        if self.__size != 0:
            [print("") for z in range(0, self.__position[1])]
        for t in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for b in range(0, self.__size)]
            if t != self.__size - 1:
                print("")
        return ("")
