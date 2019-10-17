#!/usr/bin/python3
class Student:
    """
    class that defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = {}
        if attrs is not None:
            for key in range(0, len(attrs)):
                if attrs[key] in self.__dict__:
                    my_dict[attrs[key]] = self.__dict__[attrs[key]]
                    key += 1
        else:
            for i in self.__dict__:
                my_dict[i] = self.__dict__[i]
        return my_dict

    def reload_from_json(self, json):
        my_list = list(json.keys())
        my_dic = self.__dict__
        for i in my_list:
            my_dic[i] = json.get(i)
