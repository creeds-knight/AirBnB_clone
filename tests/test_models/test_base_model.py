#!/usr/bin/python3
""" A module contatining test cases for the class BaseModel"""
import unittest
from models.base_model import BaseModel as BM
import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """ A class to test each method in the BaseModel class"""


    def test_id(self):
        self.assertTrue(uuid.UUID(BM.id, version=4))

    def test_created_at(self):
        self.assertIsInstance(BM.created_at, datetime.datetime)

    def test_updated_at(self):
        self.assertIsInstance(BM.updated_at, datetime.datetime)

    def test_save(self):
        prev_time = BM.updated_at
        BM.save(BM)
        self.assertNotEqual(prev_time, BM.updated_at)

    def test_str_(self):
        bm_instance = BM()
        expected_str = f"[BaseModel] ({bm_instance.id}) {bm_instance.__dict__}"
        self.assertEqual(str(bm_instance), expected_str)

    def test_to_dict(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"
        for key in expected_keys:
            self.assertIn(key, BM.to_dict(BM))
        crt_str = BM.to_dict(BM)['created_at']
        upt_str = BM.to_dict(BM)['updated_at']
        self.assertEqual(datetime.datetime.strptime(crt_str, iso_format), BM.created_at)
        self.assertEqual(datetime.datetime.strptime(upt_str, iso_format), BM.updated_at)

    def test_init_(self, *args, **kwargs):
        inst1 = BM(name="apedo", passion="alx SE")
        self.assertIn('created_at', inst1.__dict__)
        self.assertIn('updated_at', inst1.__dict__)
        self.assertIn('id', inst1.__dict__)
        self.assertIn('passion', inst1.__dict__)


