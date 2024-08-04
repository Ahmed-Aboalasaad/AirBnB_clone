#!/usr/bin/python3
from models.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_user_email(self):
        print(type(User.email) is str)
        print(User.email == "")
        
