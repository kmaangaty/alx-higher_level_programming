#!/usr/bin/python3
""" Defines class Student that defines
    a student by: (based on 9-student.py)"""


class Student:
    """Represent class Student that defines
    a student by: (based on 9-student.py)"""

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

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation
            of a Student instance (same as 8-class_to_json.py)

        Args:
            attrs (list):  parameter of type list.
        """
        if (type(attrs) == list and
                all(type(snf) == str for snf in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
