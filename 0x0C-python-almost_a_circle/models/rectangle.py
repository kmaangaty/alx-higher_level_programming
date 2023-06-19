#!/usr/bin/python3
"""this is class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """this is class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init new instance of class Rectangle.
        Args:
            width (int): parameter of type int.
            height (int): parameter of type int.
            x (int): parameter of type int.
            y (int): parameter of type int.
            id (int): parameter of type int.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """this is getter and setter."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this is getter and setter."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """this is getter and setter."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """this is getter and setter."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ this function will return the value of area."""
        w = self.width
        h = self.height
        return w * h

    def display(self):
        """this function will draw a shape"""
        w = self.width
        h = self.height
        if w == 0 or h == 0:
            print("")
            return

        [print("") for z in range(self.y)]
        for d in range(self.height):
            [print(" ", end="") for sh in range(self.x)]
            [print("#", end="") for am in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        this is function to update rectangle.
        Args:
            *args (ints): parameter of type list.
            **kwargs (dict): parameter of type dict.
        """
        if args and len(args) != 0:
            xh = 0
            for mot in args:
                if xh == 0:
                    if mot is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = mot
                elif xh == 1:
                    self.width = mot
                elif xh == 2:
                    self.height = mot
                elif xh == 3:
                    self.x = mot
                elif xh == 4:
                    self.y = mot
                xh += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        thi is dict formation function.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        this is stringify function.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id,
                    self.x, self.y,
                    self.width, self.height)
