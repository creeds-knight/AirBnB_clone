#!/usr/bin/python3
""" A module to test the file storage class"""
import json
import unittest
import os
from models.engine.file_storage import FileStorage as FS
from models.base_model import BaseModel as BM
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """ A class defining all testcases for filestorage class """

    def setUp(self):
        """ Initialisation of all instances for unit tests """
        self.storage = FS()
        self.file_path = "file.json"
        self.b_m = BM()
        self.u_s = User()
        self.s_t = State()
        self.c_y = City()
        self.a_y = Amenity()
        self.p_c = Place()
        self.r_v = Review()

    def tearDown(self):
        """ Resetting all unittests"""
        self.storage._FileStorage__objects.clear()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """ A test case to test the return value of all() method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ A test case to test if a new object is created"""
        obj = BM()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_new_and_all(self):
        """ A test case to check if the new object created
            is stored in the dictionary
        """
        self.storage.new(self.c_y)
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn('City.' + self.c_y.id, all_objs)

    def test_save_creates_file(self):
        """ A test case to check if the save method creates a file"""
        self.assertFalse(os.path.exists(self.file_path))
        self.storage.new(self.b_m)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_file_storage_state(self):
        """ A test case to test the file storage before items are reloaded"""
        print(FS._FileStorage__objects)
        self.assertEqual(len(self.storage.all()), 0)

    def test_save_and_reload(self):
        """ A test case to test the file storage after items are reloaded"""
        self.storage.new(self.r_v)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 1)
        self.assertIn('Review.' + self.r_v.id, all_objs)

    def test_save_reload_with_no_file(self):
        """ A test case to test reloading on non existent files"""
        self.assertFalse(os.path.exists(self.file_path))
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(all_objs, {})

    def test_reload_with_existing_file(self):
        """ A test case to test reloading on a file"""
        self.storage.new(self.c_y)
        self.storage.new(self.b_m)
        self.storage.new(self.a_y)
        self.storage.new(self.r_v)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertEqual(len(all_objs), 4)
        self.assertIn('City.' + self.c_y.id, all_objs)
        self.assertIn('BaseModel.' + self.b_m.id, all_objs)
        self.assertIn('Amenity.' + self.a_y.id, all_objs)
        self.assertIn('Review.' + self.r_v.id, all_objs)
