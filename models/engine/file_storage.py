#!/usr/bin/python3
"""Module that defines file storage class"""

from models.base_model import BaseModel
import json
from pathlib import Path


class FileStorage:
    """a class FileStorage that serializes instances to a JSON
        file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""

        key = f'{type(obj).__name__}.{obj.id}'
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as f:
            for key, obj in FileStorage.__objects.items():
                dict_rep = obj.to_dict()
                json.dump(dict_rep, f)
                f.write('\n')

    def reload(self):
        """deserializes the JSON file to __objects"""
    
        try:
            with open(FileStorage.__file_path, 'r') as f:
                for obj in f:
                    obj_dict = json.loads(obj)
                    class_obj = eval(obj_dict['__class__'])
                    instance = class_obj(obj_dict)
                    self.new(instance)
        except Exception:
            pass
