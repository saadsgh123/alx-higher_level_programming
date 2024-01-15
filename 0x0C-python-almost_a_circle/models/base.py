#!/usr/bin/python3
# saadsgh123 <sdsghouri@gmail.com>
# base.py
"""Define the class Base"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        list_dicts = []
        for o in list_objs:
            list_dicts.append(o.to_dictionary())
        with open(file_name, "w") as file:
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_obj = cls(1, 1)
            else:
                new_obj = cls(1)
            new_obj.update(**dictionary)
            return new_obj

