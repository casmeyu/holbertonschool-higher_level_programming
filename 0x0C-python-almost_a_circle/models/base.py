#!/usr/bin/python3
"""This module is for the first Base Class Model"""
import json


class Base():
    """This is the base class model
    with a counter for handeling ids

        Attributes:
            __nb_objects = counter for the ids
    """
    __nb_objects = 0

    # Static methods

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json representation of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Returns the Json representation of json_string"""
        if type(json_string) is not str:
            raise TypeError("json_string must be a string")
        if json_string is None:
            return ([])
        return json.loads(json_string)

    # Class methods

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes Json representation to a file"""
        with open(f"{cls.__name__}.json", 'w+') as f:
            obj_list = []
            if list_objs is None:
                f.write(cls.to_json_string(obj_list))
            else:
                for item in list_objs:
                    obj_list.append(cls.to_dictionary(item))
                f.write(cls.to_json_string(obj_list))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of class based on a file"""
        list_of_instances = []
        with open(f"{cls.__name__}.json", 'r') as f:
            for line in f:
                try:
                    ins = cls.from_json_string(line)
                    for item in ins:
                        list_of_instances.append(cls.create(**item))
                except Exception as e:
                    print(f"entered exception\n{e}")

        return list_of_instances

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of cls with attributes already set
            Arguements:
                cls (Class Object): class to create
                dictionary (dict): dictionary of attributes
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    # Built in Functions
    def __init__(self, id=None):
        """Initialization of Base Object
            Arguments:
                id: id for the object, if id is None then assign __nb_objects
        """
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
