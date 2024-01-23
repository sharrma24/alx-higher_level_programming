#!/usr/bin/python3
class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """
        Initialize a square with an optional size (default is 0).

        Args:
            size (number): The size of the square (float or integer).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with type and value validation.

        Args:
            value (number): The size value to set.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on their areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on their areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area of the first square is less than the area of the second square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the first square is less than or equal to the area of the second square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area of the first square is greater than the area of the second square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the first square is greater than or equal to the area of the second square."""
        return self.area() >= other.area()
