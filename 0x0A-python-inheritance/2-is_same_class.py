#!/usr/bin/python3
"""This module defines the exact same object"""


def is_same_class(obj, a_class):
    """Returns True if object is an exactly an instance of specified class"""
    return type(obj) == a_class
