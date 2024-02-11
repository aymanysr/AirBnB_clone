#!/usr/bin/python3
"""Unittest for the FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.fs = FileStorage()
        self.model = BaseModel()
        self.model.save()

    def tearDown(self):
        """Tear down for the tests"""
        os.remove("file.json")

    def test_all(self):
        """Test the all method"""
        objects = self.fs.all()
        self.assertIsInstance(objects, dict)
        self.assertIn("BaseModel." + self.model.id, objects)

    def test_new(self):
        """Test the new method"""
        new_model = BaseModel()
        self.fs.new(new_model)
        objects = self.fs.all()
        self.assertIn("BaseModel." + new_model.id, objects)

    def test_save(self):
        """Test the save method"""
        self.fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        """Test the reload method"""
        objects = self.fs.all()
        self.fs.reload()
        new_objects = self.fs.all()
        self.assertEqual(objects, new_objects)


if __name__ == '__main__':
    unittest.main()
