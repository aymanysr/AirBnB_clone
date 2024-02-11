#!/usr/bin/python"
"""test for the init file"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage

class TestInit(unittest.TestCase):
    """Test the initialization of the models package"""

    def test_storage_instance(self):
        """Test that storage is an instance of FileStorage"""
        self.assertIsInstance(storage, FileStorage)

    def test_reload_method(self):
        """Test the reload method"""
        try:
            storage.reload()
        except Exception as e:
            self.fail(f"storage.reload() raised {type(e).__name__} unexpectedly!")

if __name__ == '__main__':
    unittest.main()
