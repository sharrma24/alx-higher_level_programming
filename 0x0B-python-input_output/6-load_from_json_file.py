#!/usr/bin/python3
"""Defines a function for reading a Python object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read.
    Returns:
        The Python object created from the JSON file.
    """
    with open(filename) as f:
        return json.load(f)

