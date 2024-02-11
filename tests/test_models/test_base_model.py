#!/usr/bin/python3
"""Unittest for the BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_str_representation(self):
        model = BaseModel()
        model_str = str(model)
        self.assertIn('BaseModel', model_str)
        self.assertIn(model.id, model_str)

    def test_to_dict_datetime_format(self):
        model = BaseModel()
        modl_dict = model.to_dict()

        self.assertIsInstance(modl_dict['created_at'], str)
        self.assertIsInstance(modl_dict['updated_at'], str)
        self.assertEqual(
            datetime.strptime(modl_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"),
            model.created_at)
        self.assertEqual(
            datetime.strptime(modl_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"),
            model.updated_at)

    def test_id_generation(self):
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)
        self.assertNotEqual(model1.id, model2.id)
        self.assertTrue(uuid.UUID(model1.id, version=4))
        self.assertTrue(uuid.UUID(model2.id, version=4))

    def test_init_with_kwargs(self):
        """Test the initialization with keyword arguments"""
        model_dict = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        model = BaseModel(**model_dict)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at, datetime.strptime('2022-01-01T00:00:00.000000', "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model.updated_at, datetime.strptime('2022-01-01T00:00:00.000000', "%Y-%m-%dT%H:%M:%S.%f"))

    def test_str_method(self):
        """Test the __str__ method"""
        model = BaseModel()
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save_method(self):
        """Test the save method"""
        model = BaseModel()
        updated_at_before_save = model.updated_at
        model.save()
        self.assertNotEqual(updated_at_before_save, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict["created_at"], model.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model_dict["updated_at"], model.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"))


if __name__ == '__main__':
    unittest.main()
