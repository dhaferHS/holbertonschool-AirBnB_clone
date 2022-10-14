#!/usr/bin/python3
"""import modules"""
import json
import os

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


"""FileStorage class file"""


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """
            sets in __objects the object with key <obj class name>.id
            args:
                obj: object
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """serialize __objects to the JSON file """
        dict = {}
        for key, value in self.__objects.items():
            dict[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, "r", encoding="utf-8") as fd:
                dictj = json.load(fd)
            for key, value in dictj.items():
                FileStorage.__objects[key] = eval(value['__class__'])(**value)
