#!/usr/bin/python3
"""Defines a function to convert a Python class instance to its JSON dictionary representation."""

def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__

