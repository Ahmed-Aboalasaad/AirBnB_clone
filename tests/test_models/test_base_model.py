#!/usr/bin/python3
import unittest
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
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

    def test_correct_reload(self):
        fs = FileStorage()

        # [1] Get the storage file path
        file_path = "file.json"
        try:
            file_path = FileStorage._FileStorage__file_path
        except Exception:
            pass

        # [2] Remove any previouslys stored objects
        try:
            os.remove(file_path)
        except Exception:
            pass

        # [3] Clear the currently loaded objects in memory
        try:
            fs._FileStorage__objects.clear()
        except Exception:
            pass

        # [4] Append 10 new BaseModel objects to the __objects dict
        ids = []
        for i in range(10):
            bm = BaseModel()
            bm.updated_at = datetime.utcnow()
            fs.new(bm)
            ids.append(bm.id)

        # [5] Remove the json file (if any) and save my 10 objects
        try:
            os.remove(file_path)
        except Exception:
            pass
        fs.save()

        # [6] Clear the objects I have in memory and reload those that I saved
        try:
            fs._FileStorage__objects.clear()
        except Exception:
            pass
        fs.reload()
        all_reloaded = fs.all()

        # [7] Check for errors in the reloaded objects
        self.assertEqual(len(all_reloaded.keys()), len(ids))
        for id in ids:
            self.assertIsNotNone(
                all_reloaded.get(id) or
                all_reloaded.get("{}.{}".format("BaseModel", id))
            )

        # [8] Remove the json file
        try:
            os.remove(file_path)
        except Exception as e:
            pass


if __name__ == '__main__':
    unittest.main()
