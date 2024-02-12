#!/usr/bin/python3
"""module to test the user class """
import unittest
from models.base_model import BaseModel as BM
from models.user import User


class TestUser(unittest.TestCase):
    """ A class with unit tests defined to test User"""
    def setUp(self):
        """Initialisation for test cases"""
        self.user = User()

    def test_User_attributes(self):
        """ Test attributes for User"""

        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))

    def test_amenity_initialisation(self):
        """ A test to test amenity initialisattion"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
