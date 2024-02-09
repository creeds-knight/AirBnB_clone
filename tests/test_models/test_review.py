#!/usr/bin/python3
"""A module to test the review class """
import unittest
from models.base_model import BaseModel as BM
from models.review import Review


class TestReview(unittest.TestCase):
    """ A class with unit tests defined to test review"""
    def setUp(self):
        """Initialisation for test cases"""
        self.review = Review()

    def test_review_attributes(self):
        """ Test attributes for review"""

        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_review_initialisation(self):
        """ A test to test review initialisattion"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
