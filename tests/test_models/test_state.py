#!/usr/bin/python3
"""Unittest module for State"""
from re import S
from models.base_model import BaseModel
from models.state import State
import unittest
import pycodestyle
from datetime import datetime

class TestState(unittest.TestCase):
    """class testing the State class"""

    def test_init(self):
        """test the creation of an instance"""
        s = State()
        self.assertEqual(s.name, '')
        s.name = 'nabeul'
        self.assertEqual(s.name, 'nabeul')
        self.assertTrue(hasattr(s, 'id'))
        self.assertTrue(hasattr(s, 'created_at'))
        self.assertTrue(hasattr(s, 'updated_at'))
        self.assertTrue(issubclass(s.__class__, BaseModel))

    def test_str(self):
        """Test the string output of the class"""
        s = State()
        self.assertEqual(str(s), f"[State] ({s.id}) {s.__dict__}")


if __name__ == '__main__':
    unittest.main()
