#!/usr/bin/python3
"""Unittest for State class"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_instance_creation(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        state = State()
        state_str = str(state)
        self.assertIn('State', state_str)
        self.assertIn(state.id, state_str)

    def test_save_method(self):
        state = State()
        created_at_before_save = state.created_at
        updated_at_before_save = state.updated_at

        state.save()

        self.assertNotEqual(updated_at_before_save, state.updated_at)
        self.assertEqual(created_at_before_save, state.created_at)

    def test_to_dict_method(self):
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], "")

    def test_to_dict_datetime_format(self):
        state = State()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

    def test_init_method(self):
        state = State(name="California")
        self.assertEqual(state.name, "California")


if __name__ == '__main__':
    unittest.main()
