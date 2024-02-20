#!/usr/bin/python3
"""Defines a function for converting a string to its JSON representation."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a given object.

    Args:
        my_obj: The object to convert to JSON.
    Returns:
        A string containing the JSON representation of the object.
    """
    return json.dumps(my_obj)

