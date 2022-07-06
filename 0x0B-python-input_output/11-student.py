#!/usr/bin/python3
"""This mobule defines a student class"""


class student:
    """A class named stuednt

    Attributes:
    attr1(first_name): first name of student
    attr2(last_name): last name of student
    attr3(age): age of student
    """
    def __init__(self, first_name, last_name, age):
        """initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to _json(self, attrs=None):
        """Retrieves a dictionary representation of student"""
        if type(attrs) is list and all(type(x) is str for x in attrs):
            dictionary = {}
            for i in attrs:
                if i in self.__dict__:
                    dictionary[i] = self.__dict__[i]
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
