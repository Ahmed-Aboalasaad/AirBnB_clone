#!/usr/bin/python3
'''Contains the necessary classes for file storage'''
import json
import os
import models


class FileStorage():
    def __init__(self) -> None:
        self.__file_path = './file.json'
        self.__objects = {}
        # __objects stores objects with keys like this: <class name>.id

    def all(self) -> dict:
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        self.__objects[f'{obj.__class__}.{obj.id}'] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        # convert the __objects values from objects to dictionaries
        converted_objs = {
              key: obj.to_dict() for key, obj in self.__objects.items()
        }

        # json-dump the converted dictionary
        with open(self.__file_path, 'w') as json_file:
            json.dump(converted_objs, json_file, indent=4)

    def reload(self):
        '''deserializes the JSON file to __objects only if the JSON file
        at __file_path exists. Otherwise, does nothing'''
        # Stop the function is no such file exists
        if not os.path.exists(self.__file_path):
            return

        with open(self.__file_path, 'r') as json_file:
            all_obj_dicts = json.load(json_file)  # All objects dictionaries
            # For each one, find the class, and create it
            for key, obj_dict in all_obj_dicts.items():
                class_name = obj_dict['__class__']
                _class = models.class_registry.get(class_name, None)
                if _class:
                    self.__objects[key] = _class(**obj_dict)
