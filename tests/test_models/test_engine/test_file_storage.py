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

    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertIsInstance(self.fs.all(), dict)

    def test_new_adds_object(self):
        """Test that new adds an object to the storage"""
        new_model = BaseModel()
        self.fs.new(new_model)
        self.assertIn("BaseModel." + new_model.id, self.fs.all())

    def test_save_creates_file(self):
        """Test that save creates a file"""
        self.fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_loads_objects(self):
        """Test that reload loads objects from the file"""
        objects_before = self.fs.all()
        self.fs.reload()
        objects_after = self.fs.all()
        self.assertEqual(objects_before, objects_after)

    def test_reload_ignores_missing_file(self):
        """Test that reload doesn't raise an exception if the file doesn't exist"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        try:
            self.fs.reload()
        except FileNotFoundError:
            self.fail("reload raised FileNotFoundError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
