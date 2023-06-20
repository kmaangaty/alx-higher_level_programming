#!/usr/bin/python3
"""
this is class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    this is class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        init a new Square.
        Args:
            size (int): parameter of type int.
            x (int): parameter of type int.
            y (int): parameter of type int.
            id (int): parameter of type int.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        this is getter and setter
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        this is the update function.
        Args:
            *args (ints): parameter of type list.
            **kwargs (dict): parameter of type dict.
        """
        if args and len(args) != 0:
            mota = 0
            for mot in args:
                if mota == 0:
                    if mot is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = mot
                elif mota == 1:
                    self.size = mot
                elif mota == 2:
                    self.x = mot
                elif mota == 3:
                    self.y = mot
                mota += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        this is cord function
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        this is stringify function.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
