import unittest

from src.business_logic import can_use_makerspace


'''
Feasible paths:
1. 135 -> 148 -> 150 -> 151 -> 153 -> 154 -> 161 -> 164
2. 135 -> 148 -> 150 -> 151 -> 153 -> 155 -> 156 -> 161 -> 164
3. 135 -> 148 -> 150 -> 151 -> 153 -> 155 -> 157 -> 158 -> 159 -> 161 -> 164
4. 135 -> 148 -> 150 -> 151 -> 153 -> 155 -> 157 -> 158 -> 159 -> 161 -> 162 -> 164
'''

class TestCanUseMakerSapce(unittest.TestCase):
    def test_invalid_age(self):
        """
        Test that an invalid age (-1) prevents access to the makerspace.
        The system should return False for any negative age.
        """
        self.assertFalse(can_use_makerspace(-1,0,True))

    def test_too_young(self):
        """
        Test that a patron who is too young cannot use the makerspace.
        The system should return False for patrons below the minimum age requirement.
        """
        self.assertFalse(can_use_makerspace(10,0,True))
    
    def test_under_65_true(self):
        """
        Test that a patron within the age requirement (65) can use the makerspace.
        The system should return True as the patron meets the age and other requirements.
        """
        self.assertTrue(can_use_makerspace(64,0,True))

    def test_under_50_false(self):
        """
        Test that a patron of acceptable age with outstanding fees cannot use the makerspace.
        The system should return False when the patron does not meet fee requirements.
        """
        self.assertFalse(can_use_makerspace(49,10,True))