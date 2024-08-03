#!/usr/bin/python3
''' The code that initiates this package '''
from models.engine.file_storage import FileStorage

class_registry = {}
storage = FileStorage()
storage.reload()
