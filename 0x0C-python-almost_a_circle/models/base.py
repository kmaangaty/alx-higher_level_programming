#!/usr/bin/python3
"""Defines a class (Base)"""
import csv
import json
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
            return ged.update(**dictionary)

    @classmethod
    def load_from_file(cls):
        """
        class method (load_from_file): json formation method
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
        class method (load_from_file_csv): load from csv file
        Returns:
            result of data in file
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
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        canvas = turtle.Turtle()
        Base.init_canvas(canvas)

        for reco in list_rectangles:
            Base.morb(canvas, reco)
            for d in range(2):
                Base.rec_row(canvas, reco)
            canvas.hideturtle()

        canvas.color("#b5e3d8")
        for morcor in list_squares:
            Base.rdo(canvas, morcor)
            for y in range(2):
                Base.rdt(canvas, morcor)
            canvas.hideturtle()

        turtle.exitonclick()

    @staticmethod
    def init_canvas(cvs):
        """
        staticmethod (load_from_file_csv): load from csv file
        Args:
            cvs (turtle): parameter of type turtle.
        """
        cvs.screen.bgcolor("#b7312c")
        cvs.pensize(3)
        cvs.shape("turtle")
        cvs.color("#ffffff")

    @staticmethod
    def morb(cvs, reco):
        """
        staticmethod (load_from_file_csv): load from csv file
        Args:
            cvs (turtle): parameter of type turtle.
            reco (ldt): parameter of type ldt.
        """
        cvs.showturtle()
        cvs.up()
        cvs.goto(reco.x, reco.y)
        cvs.down()

    @staticmethod
    def rec_row(cvs, record):
        """
        staticmethod (load_from_file_csv): load from csv file
        Args:
            cvs (turtle): parameter of type turtle.
            record (ldt): parameter of type ldt.
        """
        cvs.forward(record.width)
        cvs.left(90)
        cvs.forward(record.height)
        cvs.left(90)

    @staticmethod
    def rdo(cvs, mordo):
        """
        staticmethod (load_from_file_csv): load from csv file
        Args:
            cvs (turtle): parameter of type turtle.
            mordo (ldt): parameter of type ldt.
        """
        cvs.showturtle()
        cvs.up()
        cvs.goto(mordo.x, mordo.y)
        cvs.down()

    @staticmethod
    def rdt(cvs, mordo):
        """
        staticmethod (load_from_file_csv): load from csv file
        Args:
            cvs (turtle): parameter of type turtle.
            mordo (ldt): parameter of type ldt.
        """
        cvs.forward(mordo.width)
        cvs.left(90)
        cvs.forward(mordo.height)
        cvs.left(90)
