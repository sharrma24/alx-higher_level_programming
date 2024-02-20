#!/usr/bin/python3
"""Describes a function for reading text files."""

def read_file(filename=""):
    """Displays the content of a UTF8 text file on the standard output.

    Args:
        filename (str): The name of the file to be read.
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

