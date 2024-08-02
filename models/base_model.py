#!/usr/bin/python3
'''
In this file, the base model is defined
which defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
import copy
import json


class BaseModel():
    def __init__(self) -> None:
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        string = f'[BaseModel] ({self.id}) {self.__dict__}'
        return string

    def save(self) -> None:
        self.updated_at = datetime.now()
        dict = self.to_dict()
        with open('output.json', 'w') as json_file:
            json.dump(dict, json_file, indent=4)

    def to_dict(self):
        dict = copy.deepcopy(self.__dict__)
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict
