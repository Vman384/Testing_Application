import unittest
from src.patron import Patron

class TestPatron(unittest.TestCase):
    """
    Test cases for the TestPatron class
    """
    def test_print_patron(self):
        """
        Test the __str__ method of the patron
        """
        #mock a patron
        mock_patron = Patron()
        mock_patron._id = 100
        mock_patron._name = "John Doe"
        mock_patron._age = 95
        mock_patron._outstanding_fees = 7.45
        mock_patron._gardening_tool_training = False
        mock_patron._carpentry_tool_training = False
        mock_patron._makerspace_training = False
        self.assertEqual(str(mock_patron),"Patron 100: John Doe (aged 95)\nOutstanding fees: $7.45\nCompleted training: NONE\nNo current loans")


        

