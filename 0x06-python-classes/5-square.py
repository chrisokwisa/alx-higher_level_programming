#!/usr/bin/python3
"""This module creates a class module square"""


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
        self.size = size

    def area(self):
        """Calculates the area based on size ofsquare
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * size.__size

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints in stdout the square with the # character"""
        if self.__size > 0:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
