#!/usr/bin/python3
"""This module defines append_write class"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file, returns # of characters writtern
    Args:
    filename (str): File to append to
    text (str): text to append

    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
