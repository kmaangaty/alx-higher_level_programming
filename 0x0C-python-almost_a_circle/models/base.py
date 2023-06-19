#!/usr/bin/python3
"""Defines a class (Base)"""
import json
import csv
import turtle


class Base:
    """
    this is Base class.
    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        inti a new instance of class Base.
        Args:
            id (int): parameter of type int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        static method (to_json_string): converts dicts to json
        Args:
            list_dictionaries (list): parameter of type list
        """
        if list_dictionaries is None or list_dictionaries == []:
            quote = "[]"
            return quote
        result = json.dumps(list_dictionaries)
        return result

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method (save_to_file):  write json to file
        Args:
            list_objs (list): parameter of type list
        """
        fn = cls.__name__ + ".json"
        with open(fn, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else:
                ld = [o.to_dictionary() for o in list_objs]
                jf.write(Base.to_json_string(ld))

    @staticmethod
    def from_json_string(json_string):
        """
        static method (from_json_string): that returns the list of the JSON
        string representation json_string
        Args:
            json_string (str): parameter of type str.
        Returns:
            json_string is a string representing a list of dictionaries
            If json_string is None or empty, return an empty list
            Otherwise, return the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            el = []
            return el
        result = json.loads(json_string)
        return result

    @classmethod
    def create(cls, **dictionary):
        """
        class method (create): json formation method
        Args:
            **dictionary (dict): parameter of type dict.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                ged = cls(1, 1)
            else:
                ged = cls(1)
            ged.update(**dictionary)
            return ged

    @classmethod
    def load_from_file(cls):
        """
        class method (load_from_file): json formation function
        Returns:
             returns a list of instances.
        """
        fn = str(cls.__name__) + ".json"
        try:
            with open(fn, "r") as jf:
                ld = Base.from_json_string(jf.read())
                result = [cls.create(**d) for d in ld]
                return result
        except IOError:
            el = []
            return el

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        class method (save_to_file_csv): serializes and deserializes.
        Args:
            list_objs (list): parameter of type list.
        """
        fn = cls.__name__ + ".csv"
        with open(fn, "w", newline="") as csf:
            if list_objs is None or list_objs == []:
                ikt = "[]"
                csf.write(ikt)
            else:
                if cls.__name__ == "Rectangle":
                    fdn = ["id", "width", "height", "x", "y"]
                else:
                    fdn = ["id", "size", "x", "y"]
                ktb = csv.DictWriter(csf, fieldnames=fdn)
                for it in list_objs:
                    row = it.to_dictionary()
                    ktb.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        class method (save_to_file_csv): serializes and deserializes.
        """
        fn = cls.__name__ + ".csv"
        try:
            with open(fn, "r", newline="") as csf:
                if cls.__name__ == "Rectangle":
                    fdn = ["id", "width", "height", "x", "y"]
                else:
                    fdn = ["id", "size", "x", "y"]
                ld = csv.DictReader(csf, fieldnames=fdn)
                ld = [dict([k, int(v)] for k, v in d.items())
                      for d in ld]
                return [cls.create(**d) for d in ld]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        static method (draw): function to draw shape.

        Args:
            list_rectangles (list): parameter of type list
            list_squares (list): parameter of type list
        """
        rsm = turtle.Turtle()
        rsm.screen.bgcolor("#b7312c")
        rsm.pensize(3)
        rsm.shape("turtle")

        rsm.color("#ffffff")
        for rect in list_rectangles:
            rsm.showturtle()
            rsm.up()
            rsm.goto(rect.x, rect.y)
            rsm.down()
            for i in range(2):
                rsm.forward(rect.width)
                rsm.left(90)
                rsm.forward(rect.height)
                rsm.left(90)
            rsm.hideturtle()

        rsm.color("#b5e3d8")
        for sq in list_squares:
            rsm.showturtle()
            rsm.up()
            rsm.goto(sq.x, sq.y)
            rsm.down()
            for i in range(2):
                rsm.forward(sq.width)
                rsm.left(90)
                rsm.forward(sq.height)
                rsm.left(90)
            rsm.hideturtle()

        turtle.exitonclick()
