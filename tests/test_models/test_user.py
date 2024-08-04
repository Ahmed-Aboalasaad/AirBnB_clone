#!/usr/bin/python3
from models.user import User
import unittest

class TestUser(unittest.TestCase):
    def test_user_email(self):
        self.assertIs(type(User.email), str)
        self.assertEqual(User.email, "")

if __name__ == '__main__':
    unittest.main()
