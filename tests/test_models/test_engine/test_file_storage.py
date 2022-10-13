#!/usr/bin/python3
"""unit tests for FileStorage class"""

import unittest
import os
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTests(unittest.TestCase):
    """
    Class FileStorageTests that provides unit testing for the
    FileStorage class"""
    

    def test_init(self):
        """
        Method for testing initialization of the FileStorage class.
        """
        self.assertIsNotNone(self.fs1)
        self.assertIsInstance(self.fs1, FileStorage)
        self.assertIsNotNone(self.fs1._FileStorage__file_path)
        self.assertEqual(self.fs1._FileStorage__file_path, "file.json")
        self.assertIsNotNone(self.fs1._FileStorage__objects)
        self.assertIsInstance(self.fs1._FileStorage__objects, dict)

    def test_all(self):
        """
        Method for testing functionality of the all method
        of the FileStorage class."""
        self.assertIsNotNone(self.fs1.all())
        self.assertIsInstance(self.fs1.all(), dict)
        self.fs1.new(self.bm1)
        key = f'BaseModel.{self.bm1.id}'
        self.assertIsNotNone(self.fs1.all(), {key: self.bm1})

    def test_new(self):
        """Tests if new updates the private dictionary __objects
           accessed with all with a created BaseModel instance"""

        storage = FileStorage()
        my_model = BaseModel()
        objects = storage.all()
        self.assertTrue(my_model in objects.values())

    def test_save(self):
        """Tests if save creates a JSON file if it doesn't exist"""

        storage = FileStorage()
        storage.save()
        self.assertTrue(exists(TestFileStorage.__file_path))

    def test_reload(self):
        """Tests if the created JSON file is updated each time save
           is called and that reload loads in the previouly created
           objects stored in the JSON file"""

        storage = FileStorage()
        storage.save()
        with open(TestFileStorage.__file_path, 'r') as file_1:
            file_data_1 = json.load(file_1)
        my_model_1 = BaseModel()
        storage.save()
        with open(TestFileStorage.__file_path, 'r') as file_2:
            file_data_2 = json.load(file_2)
        self.assertNotEqual(file_data_1, file_data_2)

        all_1 = storage.all()
        storage.reload()
        all_2 = storage.all()
        self.assertEqual(all_1, all_2)
         
if __name__ == '__main__':
    unittest.main()
