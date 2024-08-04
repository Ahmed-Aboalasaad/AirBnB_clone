#!/usr/bin/python3
'''Doc: In this file, the User class is defined'''
from models.base_model import BaseModel


class User(BaseModel):
    email = ''
    password = ''
    first_name = ''
    last_name = ''
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        if 'email' in kwargs:
            self.email = kwargs['email']
        if 'password' in kwargs:
            self.password = kwargs['password']
        if 'first_name' in kwargs:
            self.first_name = kwargs['first_name']
        if 'last_name' in kwargs:
            self.last_name = kwargs['last_name']

    def to_dict(self) -> dict:
        new_dict = super().to_dict()
        new_dict['email'] = self.email
        new_dict['password'] = self.password
        new_dict['first_name'] = self.first_name
        new_dict['last_name'] = self.last_name
        return new_dict
