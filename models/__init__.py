#!/usr/bin/python3
'''Package Documentation: 'models' package '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

# class registery to have references to all classes so that we reload properly
class_registry = {}
class_registry['BaseModel'] = BaseModel

storage = FileStorage()
storage.reload()
