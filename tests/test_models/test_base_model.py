#!/usr/bin/python3
""" Unittest for class BaseModel """


import unittest
import pycodestyle
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test for pycodestyle"""
    

    def test_id(self):
        """Test attribute id"""
        b1 = BaseModel()
        b2 = BaseModel(None)
        b3 = BaseModel("name")
        b4 = BaseModel(3)
        b5 = BaseModel(2.2)
        b6 = BaseModel(float('information'))
        b7 = BaseModel([1, 2, 3])
        b8 = BaseModel({"name": "diy", "age": 20})

        self.assertRegex(b1.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b2.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b3.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b4.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b5.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b6.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b7.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b8.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")

    def test_created_at(self):
        """Test attribute created_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel(None)
        b4 = BaseModel(3)
        b5 = BaseModel(3.2)
        b6 = BaseModel("John")
        b7 = BaseModel(float('information'))
        b8 = BaseModel([1, 2, 3])
        b9 = BaseModel({"name": "diy", "age": 20})

        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertRegex(b1.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b3.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b4.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b5.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b6.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b7.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b8.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b9.created_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")

    def test_updated_at(self):
        """Test attribute updated_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel(None)
        b4 = BaseModel(3)
        b5 = BaseModel(3.2)
        b6 = BaseModel("Lucile")
        b7 = BaseModel(float('information'))
        b8 = BaseModel([1, 2, 3])
        b9 = BaseModel({"name": "diy", "age": 20})

        self.assertNotEqual(b1.updated_at, b2.updated_at)
        self.assertRegex(b1.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b3.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b4.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b5.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b6.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b7.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b8.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b9.updated_at.isoformat(),
                         "[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")

    def test_str(self):
        """Test the __str__ method"""
        b1 = BaseModel()
        b2 = BaseModel(None)
        b3 = BaseModel("name")
        b4 = BaseModel(3)
        b5 = BaseModel(2.5)
        b6 = BaseModel(float('information'))
        b7 = BaseModel([1, 2, 3])
        b8 = BaseModel({"name": "diy", "age": 20})

        self.assertEqual(str(b1), f"[{b1.__class__.__name__}] ({b1.id}) " +
                         f"{b1.__dict__}")
        self.assertEqual(str(b2), f"[{b2.__class__.__name__}] ({b2.id}) " +
                         f"{b2.__dict__}")
        self.assertEqual(str(b3), f"[{b3.__class__.__name__}] ({b3.id}) " +
                         f"{b3.__dict__}")
        self.assertEqual(str(b3), f"[{b3.__class__.__name__}] ({b3.id}) " +
                         f"{b3.__dict__}")
        self.assertEqual(str(b4), f"[{b4.__class__.__name__}] ({b4.id}) " +
                         f"{b4.__dict__}")
        self.assertEqual(str(b5), f"[{b5.__class__.__name__}] ({b5.id}) " +
                         f"{b5.__dict__}")
        self.assertEqual(str(b6), f"[{b6.__class__.__name__}] ({b6.id}) " +
                         f"{b6.__dict__}")
        self.assertEqual(str(b7), f"[{b7.__class__.__name__}] ({b7.id}) " +
                         f"{b7.__dict__}")
        self.assertEqual(str(b8), f"[{b8.__class__.__name__}] ({b8.id}) " +
                         f"{b8.__dict__}")

    def test_save(self):
        """Test __save__ method"""
        b1 = BaseModel()
        b1.save()
        b2 = BaseModel(None)
        b2.save()
        b3 = BaseModel("name")
        b3.save()
        b4 = BaseModel(3)
        b4.save()
        b5 = BaseModel(2.5)
        b5.save()
        b6 = BaseModel(float('information'))
        b6.save()
        b7 = BaseModel([1, 2, 3])
        b7.save()
        b8 = BaseModel({"name": "diy", "age": 20})
        b8.save()

        self.assertNotEqual(b1.created_at, b1.updated_at)
        self.assertNotEqual(b2.created_at, b2.updated_at)
        self.assertNotEqual(b3.created_at, b3.updated_at)
        self.assertNotEqual(b4.created_at, b4.updated_at)
        self.assertNotEqual(b5.created_at, b5.updated_at)
        self.assertNotEqual(b6.created_at, b6.updated_at)
        self.assertNotEqual(b5.created_at, b7.updated_at)
        self.assertNotEqual(b6.created_at, b8.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        b1 = BaseModel()
        b2 = b1.to_dict()

        self.assertEqual(b1.id, b2['id'])


if __name__ == '__main__':
    unittest.main()