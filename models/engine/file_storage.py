#!/usr/bin/python3
'''Contains the necessary classes for file storage'''
import json
import os
import models


class FileStorage():
	def __init__(self) -> None:
		self.__file_path = './file.json'
		# Stores objects with keys like this: <class name>.id
		self.__objects = {}

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
		'''deserializes the JSON file to __objects (only if the JSON file
		at __file_path exists. Otherwise, does nothing'''
		# Stop the function is no such file exists
		if not os.path.exists(self.__file_path):
			print('didn\'t find such a file path')
			return

		print('+++ Reloading +++')
		with open(self.__file_path, 'r') as json_file:
			objects_dict = json.load(json_file)  # All objects dictionaries
			# For each one, find the class, and create it
			for key, obj in objects_dict.items():
				class_name = obj['__class__']
				_class = models.class_registry.get(class_name, None)
				if _class:
					self.__objects[key] = _class(**obj)
				else:
					print('didnt find such a class in the registry')
					print(f'extracted class name: {class_name}')
					print(f'Class registry: {models.class_registry}')