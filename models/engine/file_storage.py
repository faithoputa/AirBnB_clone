#!/usr/bin/python3
"""
FileStorage module
"""


import os
import json
from models.base_model import BaseModel


class FileStorage:
    """ File  storage class """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Public instance method all
        Arg:
            self. allows you have access to the module object
            returns the dictionary __objects
        """
        return (self.__objects)

    def new(self, obj):
        """new public instance method of the module
        Arg:
            self and obj
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}{}".format(obj_cls_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ save Public instance method of the module
        Arg:
            Self
        """
        all_objs = self.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """ reload public instance method
        Arg: 
            self
        """
        if os.path.isfile(self.__file_path):
            try:
                obj_dict = json.load(file)
                for key, value in obj_dict.item():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    instance = cls(**value)
                    self.__objects[key] = instance
            except Exception:
                pass
