#!/usr/bin/python3
"""Unittest for amenity.py"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertEqual(amenity.name, "")

    def test_inheritance(self):
        amenity = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_init_method(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_init_method_with_args(self):
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_to_dict_method(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")

    def test_to_dict_datetime_format(self):
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

    def test_str_representation(self):
        amenity = Amenity()
        amenity_str = str(amenity)
        self.assertIn('Amenity', amenity_str)
        self.assertIn(amenity.id, amenity_str)


if __name__ == '__main__':
    unittest.main()
