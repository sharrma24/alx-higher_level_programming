#!/usr/bin/python3
"""Specifies a function for reading text files."""

def read_file(filename=""):
        """Display the content of a UTF8 text file on the standard output."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
