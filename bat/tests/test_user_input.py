import unittest
import src.user_input 
from unittest import mock

class TestUserInput(unittest.TestCase):
    @mock.patch('src.user_input.read_string')
    def test_is_float_true(self, readstr):
        readstr.returnValue = '1.0'
        self.assertEqual(src.user_input.read_float(''),1.0)

    def test_is_float_false(self):
        self.assertFalse(src.user_input.is_float('abc'))