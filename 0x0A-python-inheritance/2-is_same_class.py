#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a given class.

    Args:
        obj: Any object to check.
        a_class: The specified class.

    Returns:
        True if obj is exactly an instance of a_class; otherwise, False.
    """
    return type(obj) == a_class

