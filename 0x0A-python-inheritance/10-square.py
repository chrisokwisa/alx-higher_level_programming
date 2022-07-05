#!/usr/bin/python3
"""This mudule creates a Square class that inherits from rectangle"""


Rectangle = __import__('10-square').Square


class Square(Rectangle):
    """A class named square

    Attributes:
    attr1:(size): size of square
    attr2:(area): finds the area of square
    """
    def __init__(self, size):
        """initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
