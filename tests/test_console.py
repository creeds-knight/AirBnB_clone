#!/usr/bin/python3
""" A module to test the console program"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """ Unit test cases"""
    def setUp(self):
        self.console = HBNBCommand()

    def test_prompt(self):
        self.assertEqual("(hbnb)",  self.console.prompt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        self.assertTrue(self.console.onecmd('quit'))
        self.assertEqual('\n', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.assertIsNone(self.console.onecmd(''))
        self.assertEqual('', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        self.assertTrue(self.console.onecmd('EOF'))
        self.assertEqual('\n', mock_stdout.getvalue())

    def test_do_create(self):
        """ A method to test the create function """
        pass
