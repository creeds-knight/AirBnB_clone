#!/usr/bin/python3
"""A module to test the city class """
import unittest
from models.base_model import BaseModel as BM
from models.city import City


class TestCity(unittest.TestCase):
    """ A class with unit tests defined to test city"""
    def setUp(self):
        """Initialisation for test cases"""
        self.city = City()

    def test_city_attributes(self):
        """ Test attributes for city"""

        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_city_initialisation(self):
        """ A test to test city initialisattion"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")
