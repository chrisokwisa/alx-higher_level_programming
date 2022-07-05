#!/usr/bin/python3
"""This module defines a rectangle"""


BaseGeonetry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class named a BaseGeometry

    Attributes:
    attr1(width): width of a rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width, height):
        """initializes the instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
