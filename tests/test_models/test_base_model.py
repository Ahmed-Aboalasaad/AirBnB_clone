#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        self.assertIsInstance(BaseModel(), BaseModel)

    def test_str(self):
        self.assertTrue(str(BaseModel()).startswith('[BaseModel]'))

    def test_save(self):
        myObj = BaseModel()
        myObj.save()
        self.assertNotEqual(myObj.updated_at, datetime.now())

    def test_to_dict(self):
        myObj = BaseModel()
        my_dict = myObj.to_dict()
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
