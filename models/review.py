#!/usr/bin/python3
'''Doc: Contains the Review class'''
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class for Reviews'''
    place_id = ''
    user_id = ''
    text = ''
