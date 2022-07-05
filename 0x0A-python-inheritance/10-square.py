#!/usr/bin/python3
<<<<<<< HEAD
"""This module creates a class named Square"""
=======
"""This mudule creates a Square class"""
>>>>>>> baf65daacee2eac13157d4b4778e3c4cc7b83f94


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class named Square

    Attributes:
    attr1(size): size of square
    attr2(area): finds the area of it
    """
    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
