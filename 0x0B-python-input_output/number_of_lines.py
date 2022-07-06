#!/usr/bin/python3
""" Module of number of lines """


def number_of_lines(filename=""):
    """ Count the number of lines """
    cont = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            cont += 1
    return(cont)
