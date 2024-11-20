import json
import unittest
from unittest.mock import patch
from src import config
from src.data_mgmt import DataManager
import src.business_logic as business_logic


class TestCanBorrowCarpentryTool(unittest.TestCase):
    """
    Test cases for borrowing carpentry tools.
    """

    def test_senior_patron_without_training(self):
        """
        Test if a senior patron (age 70) without carpentry tool training cannot borrow a carpentry tool for a short loan.
        """
        self.assertFalse(business_logic.can_borrow_carpentry_tool(patron_age=70, length_of_loan=1, outstanding_fees=0, carpentry_tool_training=False))
    
    def test_senior_patron_too_long(self):
        """
        Test if a senior patron (age 60) without carpentry tool training cannot borrow a carpentry tool for an excessive loan length (15 days).
        """
        self.assertFalse(business_logic.can_borrow_carpentry_tool(patron_age=60, length_of_loan=15, outstanding_fees=0, carpentry_tool_training=False))


class TestTypeOfPatron(unittest.TestCase):
    """
    Test cases for determining the type of patron based on their age.
    """

    def test_elderly(self):
        """
        Test if a patron of age 100 is classified as 'Elderly'.
        """
        self.assertEqual(business_logic.type_of_patron(100), "Elderly")
    
    def test_error(self):
        """
        Test if an invalid age (-1) returns 'ERROR'.
        """
        self.assertEqual(business_logic.type_of_patron(-1), "ERROR")


class TestCalculateDiscount(unittest.TestCase):
    """
    Test cases for calculating discounts based on patron conditions.
    """

    def test_error(self):
        """
        Test if an invalid value (-1) for discount calculation returns 'ERROR'.
        """
        self.assertEqual(business_logic.calculate_discount(-1), "ERROR")


class TestCanBorrow(unittest.TestCase):
    """
    Test cases for the can_borrow function, which checks if a patron can borrow an item based on various conditions.
    """

    # def test_borrow_book(self):
    #     result = business_logic.can_borrow("Book", 25, 14, 0, False, False)
    #     self.assertTrue(result)  

    def test_borrow_book_with_fees(self):
        """
        Test if a patron cannot borrow a book if they have outstanding fees.
        """
        result = business_logic.can_borrow("Book", 25, 14, 1, False, False)
        self.assertFalse(result) 
    
    def test_borrow_book_too_long(self):
        """
        Test if a patron cannot borrow a book for an excessive loan period (60 days).
        """
        result = business_logic.can_borrow("Book", 25, 60, 0, False, False)
        self.assertFalse(result) 
    
    # def test_borrow_gardening_tool_with_training(self):
    #     """
    #     Test if a patron with gardening tool training can borrow a gardening tool.
    #     """
    #     result = business_logic.can_borrow("Gardening tool", 30, 7, 0, True, False)
    #     self.assertTrue(result)
    
    def test_borrow_gardening_tool_without_training(self):
        """
        Test if a patron without gardening tool training cannot borrow a gardening tool.
        """
        result = business_logic.can_borrow("Gardening tool", 30, 7, 0, False, False)
        self.assertFalse(result) 

    def test_borrow_gardening_tool_with_fees(self):
        """
        Test if a patron cannot borrow a gardening tool if they have outstanding fees.
        """
        result = business_logic.can_borrow("Gardening tool", 30, 7, 5, False, False)
        self.assertFalse(result)

    def test_borrow_gardening_tool_too_long(self):
        """
        Test if a patron cannot borrow a gardening tool for an excesslong loan period (30 days).
        """
        result = business_logic.can_borrow("Gardening tool", 30, 30, 0, False, False)
        self.assertFalse(result)
    
    def test_borrow_carpentry_tool_without_training(self):
        """
        Test if a patron without carpentry tool training cannot borrow a carpentry tool.
        """
        result = business_logic.can_borrow("Carpentry tool", 20, 10, 0, False, False)
        self.assertFalse(result)  
    
    def test_invalid_item_type(self):
        """
        Test if an invalid item type (string) cannot be borrowed.
        """
        result = business_logic.can_borrow("Random", 22, 5, 0, False, False)
        self.assertFalse(result)  
