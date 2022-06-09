#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if i == search else i for in my_list]
