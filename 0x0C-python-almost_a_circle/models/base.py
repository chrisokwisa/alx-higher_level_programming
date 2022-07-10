#!/usr/bin/python3
""" Base Module """


import json
import csv
import turtle


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to_json_string method """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file method """
        with open(cls.__name__ + ".json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dicts = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON strings """
        if type(json_string) != str and json_string is not None:
            raise TypeError
        if json_string is None or json_string == "[]" or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """ Method that return a list of instances """
        list_aux = []
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                inst = f.read()
        except:
            inst = '[]'
        inst2 = cls.from_json_string(inst)
        if inst2:
            for i in inst2:
                list_aux.append(cls.create(**i))
        return list_aux

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv method """
        if list_objs is None or list_objs == []:
            csvfile.write("[]")
        with open(cls.__name__ + ".csv", "w",) as f:
            if cls.__name__ == "Rectangle":
                field_names = ["id", "width", "height", "x", "y"]
            else:
                field_names = ["id", "size", "x", "y"]
            writer = csv.DictWriter(f, fieldnames=field_names)
            for objs in list_objs:
                writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv method """
        res = []
        dic = {}
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                if cls.__name__ == "Rectangle":
                    field_names = ['id', 'width', 'height', 'x', 'y']
                else:
                    field_names = ['id', 'size', 'x', 'y']
                reader = csv.DictReader(f, fieldnames=field_names)
                for rows in reader:
                    for key, v in dict(rows).items():
                        dic[key] = int(v)
                    res.append(cls.create(**dic))
        except:
            return "[]"
        return res
