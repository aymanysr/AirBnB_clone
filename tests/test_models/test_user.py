import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up for the tests"""
        self.user = User()

    def test_is_instance(self):
        """Test if user is an instance of BaseModel and User"""
        self.assertIsInstance(self.user, BaseModel)
        self.assertIsInstance(self.user, User)

    def test_init(self):
        """Test the initialization of user attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attr_types(self):
        """Test the types of the attributes of User"""
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save(self):
        """Test the save method"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

if __name__ == '__main__':
    unittest.main()
