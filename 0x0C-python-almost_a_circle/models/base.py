#!/usr/bin/python3
"""Module for Base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """Updates instance attributes with provided values"""
        if args:
            attr_names = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attr_names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file and returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                dict_list = json.loads(json_str)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
