#!/usr/bin/python3
"""This module defines a only sub class of"""


def inherits_from(obj, a_class):
    """Returns True or False is inherited directly or indirectly"""
    if isinstance(obj, a_class) is True and type(obj) != a_class:
        return True
    else:
        return False
