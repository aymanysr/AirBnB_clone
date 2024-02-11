#!/usr/bin/python3
"""class for the city"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_inheritance(self):
        city = City()
        self.assertTrue(issubclass(City, BaseModel))

    def test_init_method(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_init_method_with_args(self):
        city = City(state_id="123", name="New York")
        self.assertEqual(city.state_id, "123")
        self.assertEqual(city.name, "New York")

    def test_to_dict_method(self):
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")

    def test_to_dict_datetime_format(self):
        city = City()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

    def test_str_representation(self):
        city = City()
        city_str = str(city)
        self.assertIn('City', city_str)
        self.assertIn(city.id, city_str)


if __name__ == '__main__':
    unittest.main()
