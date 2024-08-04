#!/usr/bin/python3
'''Package Documentation: 'models' package '''
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# class registery to have references to all classes so that we reload properly
class_registry = {}
class_registry['BaseModel'] = BaseModel
class_registry['User'] = User
class_registry['State'] = State
class_registry['City'] = City
class_registry['Amenity'] = Amenity
class_registry['Review'] = Review

storage = FileStorage()
storage.reload()
