#!/usr/bin/python3
"""This class square that defines a square"""


class square:
    """A class named square
    Attributes:
    attr1 (size): size  of square
    """
    def __init__(self, size=0):
        """
        Args:
        size: attribute __size of a square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
