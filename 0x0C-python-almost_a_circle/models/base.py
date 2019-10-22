#!/usr/bin/python3
"""
fref
"""
import os.path
import json


class Base:
    """
    sdfdrf
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None and len(list_objs) > 0:
            empty_list = []
            for i in list_objs:
                my_dict = i.to_dictionary()
                empty_list.append(my_dict)
            with open(cls.__name__ + ".json", mode='w', encoding="utf-8") as f:
                    f.write(cls.to_json_string(empty_list))
        else:
            with open(cls.__name__ + ".json", mode='w', encoding="utf-8") as f:
                    f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        empty_list = []
        if json_string is None:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(5, 4, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        new_list = []
        if os.path.isfile(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", encoding="utf-8") as f:
                dicts = cls.from_json_string(f.read())
                for i in dicts:
                    instances = cls.create(**i)
                    new_list.append(instances)
                return new_list
        else:
            return new_list
