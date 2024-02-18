#!/usr/bin/python3
class MyList(list):
    """
    MyList class inherits from the built-in list class.

    Public instance method:
    - print_sorted(self): prints the list in ascending order.
    """

    def print_sorted(self):
        """Print the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
