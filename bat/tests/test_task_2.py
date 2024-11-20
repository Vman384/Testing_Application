import unittest

from src.business_logic import can_borrow_carpentry_tool

'''
Possible tests:

1. patron_age=100, length_of_loan=15, outstanding_fees=0, carpentry_tool_training=False, results = False
2. patron_age=-1, length_of_loan=15, outstanding_fees=0, carpentry_tool_training=False, results = ERROR
3. patron_age=60, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True, results = True
4. patron_age=60, length_of_loan=1, outstanding_fees=1, carpentry_tool_training=True, results = False
5. patron_age=10, length_of_loan=1, outstanding_fees=1, carpentry_tool_training=True, results = False
6. patron_age=10, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True, results = False


Possible optimal sets of tests using MC/DC:
age = {1, 3, 4, 5}
fees = {3, 4, 5}
1. patron_age=100, length_of_loan=15, outstanding_fees=0, carpentry_tool_training=False, results = False
3. patron_age=60, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True, results = True
4. patron_age=60, length_of_loan=1, outstanding_fees=1, carpentry_tool_training=True, results = False
5. patron_age=10, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True, results = False
'''

class TestCanBorrowCarpentryTool(unittest.TestCase):
    def test_patron_too_young(self):
        """
        Test that a patron who is too young cannot borrow a carpentry tool.
        The system should return False as the patrons age is below the allowed limit.
        """
        self.assertFalse(can_borrow_carpentry_tool(patron_age=10, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True))

    def test_patron_too_old(self):
        """
        Test that a patron who is too old cannot borrow a carpentry tool.
        The system should return False as the patrons age is above the allowed limit.
        """
        self.assertFalse(can_borrow_carpentry_tool(patron_age=100, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True))

    def test_valid_senior_patron(self):
        """
        Test that a senior category patron within the acceptable age range can borrow a carpentry tool.
        The system should return True when the patron meets all requirements.
        """
        self.assertTrue(can_borrow_carpentry_tool(patron_age=60, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=True))

    def test_senior_patron_with_fees(self):
        """
        Test that a senior patron with outstanding fees cannot borrow a carpentry tool.
        The system should return False as there are outstanding fees.
        """
        self.assertFalse(can_borrow_carpentry_tool(patron_age=60, length_of_loan=15, outstanding_fees=1, carpentry_tool_training=True))

if __name__ == '__main__':
    unittest.main()