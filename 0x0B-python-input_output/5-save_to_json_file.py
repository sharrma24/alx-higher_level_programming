#!/usr/bin/python3
"""Defines a function for writing an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write a Python object to a text file using its JSON representation.

    Args:
        my_obj: The Python object to be written.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)

