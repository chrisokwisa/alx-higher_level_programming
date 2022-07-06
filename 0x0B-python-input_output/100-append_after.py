#!/usr/bin/python3
""" Module for append after """


def append_after(filename="", search_string="", new_string=""):
    """ append a string into a new_line """
    aux = ""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines:
        if line.find(search_string) != -1:
            aux += line + new_string
        else:
            aux += line
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(aux)
