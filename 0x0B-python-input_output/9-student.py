#!/usr/bin/python3
"""Defines class Student that defines a student by:

Public instance attributes:
first_name
last_name
age."""


class Student:
    """Represent a student.
        class Student that defines a student by:

        Public instance attributes:
        first_name
        last_name
        age"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of class Student.
        Args:
            first_name (str): parameter of type (str).
            last_name (str): parameter of type (str).
            age (int): parameter of type (int).
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation
            of a Student instance (same as 8-class_to_json.py
            """
        return self.__dict__
