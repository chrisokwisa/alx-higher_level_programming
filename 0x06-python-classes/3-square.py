#!/usr/bin/python3
"""This module creates a class named square"""


class square:
    """A class named square

    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise valueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculation of the area based on the size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * self.__size
