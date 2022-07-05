#!/usr/bin/python3
"""
This module creates aclass named MyInt
"""


class MyInt(int):
    """
    A class named MyInt
    """

    def __eq__(self, other):
        """swaps the eq builtin"""
        return int.__ne__(self, other)
