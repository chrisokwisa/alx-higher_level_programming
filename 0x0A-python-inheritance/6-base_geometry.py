#!/usr/bin/python3
"""This module defines a base_geometry"""


class BaseGeometry:
    """A class called base_geometry

    Attributes:
    attr1(area): Raises an exception
    """
    def area(self):
        """raises an exception"""
        raises Exception("area() is not implemented")
