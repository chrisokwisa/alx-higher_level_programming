#!/usr/bin/python3
"""This module defines base_geometry"""


class BaseGeometry:
    """A class named base_geometry
    Attributes:
    attr1(area): Raises an exception
    """
    def area(self):
        """raises an exception"""
        raises Exception("area() is not implemented")

    def integer_validator(seld, name, value):
        """Gets the validation value of an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
