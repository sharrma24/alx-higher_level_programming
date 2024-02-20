#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attributes=None):
        """Get a dictionary representation of the Student.

        If attributes is a list of strings, represents only those attributes
        included in the list.

        Args:
            attributes (list): (Optional) The attributes to represent.
        """
        if (type(attributes) == list and
                all(type(ele) == str for ele in attributes)):
            return {key: getattr(self, key) for key in attributes if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replace all attributes of the Student.

        Args:
            json_data (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json_data.items():
            setattr(self, key, value)

