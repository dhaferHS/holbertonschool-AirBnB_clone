#!/usr/bin/python3
"""unit tests for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorageTests(unittest.TestCase):
    """
    Class FileStorageTests that provides unit testing for the
    `FileStorage` class.
    """
    

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
        of the FileStorage class.
        """
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

    
         
if __name__ == '__main__':
    unittest.main()
