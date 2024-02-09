#!/usr/bin/python3
"""A module to test the amenity class """
import unittest
from models.base_model import BaseModel as BM
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ A class with unit tests defined to test amenity"""
    def setUp(self):
        """Initialisation for test cases"""
        self.amenity = Amenity()

    def test_amenity_attributes(self):
        """ Test attributes for amenity"""

        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_amenity_initialisation(self):
        """ A test to test amenity initialisattion"""
        self.assertEqual(self.amenity.name, "")
