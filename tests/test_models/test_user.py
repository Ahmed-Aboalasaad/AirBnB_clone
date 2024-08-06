#!/usr/bin/python3
from models.user import User
import unittest


class TestUser(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(User(), User)

    def test_user_datatypes(self):
        self.assertIs(type(User.email), str)
        self.assertIs(type(User.password), str)
        self.assertIs(type(User.first_name), str)
        self.assertIs(type(User.last_name), str)

    def test_to_dict(self):
        self.assertEqual(User().to_dict()['__class__'], 'User')


if __name__ == '__main__':
    unittest.main()
