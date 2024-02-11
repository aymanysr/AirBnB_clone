#!/usr/bin/python3
"""
Class for FileStorage
"""

import json
from models.base_model import BaseModel
from models.user import User

class_dict = {"BaseModel": BaseModel, "User": User}


class FileStorage:
    """
    FileStorage class that serial and deserializes instances
    to a JSON file and vice versa
    """

    __file_path = "file.json"  # path to the JSON file
    __objects = {}  # empty dictionary to store all objects by <class name>.id

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file (path: __file_path)
        """
        json_objs = {}
        for key, value in self.__objects.items():
            json_objs[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(json_objs, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file exists; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)

            for key, value in json_obj.items():
                self.__objects[key] = class_dict[value["__class__"]](**value)

        except FileNotFoundError:
            pass
