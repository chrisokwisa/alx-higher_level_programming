#!/usr/bin/python3
""" Module for pascal triangle """


def pascal_triangle(n):
    """ Pascal triangle """
    tri = []
    ini = 1
    for i in range(0, n):
        rows = []
        for j in range(0, i + 1):
            if i == 0 or j == 0 or (i > 0 and j == i):
                rows.append(ini)
            else:
                rows.append(tri[i - 1][j] + tri[i - 1][j - 1])
        tri.append(rows)
    return tri
