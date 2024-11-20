import unittest

from src.borrowable_item import BorrowableItem

class TestBorrowableItem(unittest.TestCase):
    """
    Tests for the BorrowableItem class
    """
    def test_print_borrowable_item(self):
        """
        Test the __str__ method of the borrowable item
        """
        
        # Mock a catalogue item
        mock_item = BorrowableItem()
        mock_item._id = 100
        mock_item._name = "Hammer"
        mock_item._type = "Carpentry tool"
        mock_item._year = 2020
        mock_item._number_owned = 5
        mock_item._on_loan = 2
        self.assertEqual(str(mock_item),"Item 100: Hammer (Carpentry tool)\nYear: 2020\n2/5 on loan")