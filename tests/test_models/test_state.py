#!/usr/bin/python3
"""A module to test the state class """
import unittest
from models.base_model import BaseModel as BM
from models.state import State


class TestState(unittest.TestCase):
    """ A class with unit tests defined to test state"""
    def setUp(self):
        """Initialisation for test cases"""
        self.state = State()

    def test_state_attributes(self):
        """ Test attributes for state"""

        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))

    def test_state_initialisation(self):
        """ A test to test state initialisattion"""
        self.assertEqual(self.state.name, "")
