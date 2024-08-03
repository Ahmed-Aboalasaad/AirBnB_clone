#!/usr/bin/python3
'''
In this file, the base model is defined
which defines all common attributes/methods for other classes
'''
import uuid
from datetime import datetime
import copy
from models import storage
from models import class_registry


class BaseModel():
    def __init__(self, *args, **kwargs) -> None:
        # some keyword arguments were passed.. I add them to the class
        if (kwargs):
            # Remove the __class__ attribute (if any)
            kwargs.pop('__class__', None)

            # Handle datetime strings
            # add them as parsed objects and remove the strings
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            kwargs.pop('created_at', None)
            kwargs.pop('updated_at', None)

            # add the remaining attributes
            for key, value in kwargs.items():
                setattr(self, key, value)

        # empty argument list (new instance)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self) -> str:
        string = f'[BaseModel] ({self.id}) {self.__dict__}'
        return string

    def save(self) -> None:
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict = copy.deepcopy(self.__dict__)
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        return dict


class_registry["BaseModel"] = BaseModel
print('----- Added to the class registry ------')