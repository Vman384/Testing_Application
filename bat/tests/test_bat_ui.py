import unittest
from unittest.mock import patch

from src.bat_ui import BatUI
from src.data_mgmt import DataManager


class TestLoanItem(unittest.TestCase):
    @patch('src.user_input.read_string')
    def test_loan_item_item_not_found(self, readstr):
        """
        Test attempting to loan an item that does not exist in the catalogue.
        The system should output a cancellation message and return to the main menu.
        """
        readstr.side_effect = ['1','99999999999']
        
        
        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()

        
        self.assertEqual("MAIN MENU", ui.get_current_screen())

    @patch('src.user_input.read_string')
    def test_loan_item_cancel(self, readstr):
        """
        Test cancelling the loan operation before it is completed.
        The system should output a cancellation message and return to the main menu.
        """
        readstr.side_effect = ['1','1', 'n']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()


        
        self.assertEqual("MAIN MENU", ui.get_current_screen())

    
    @patch('src.user_input.read_string')
    def test_loan_item_no_such_patron(self, readstr):
        """
        Test attempting to loan an item to a patron that does not exist.
        The system should output a message that no such patron exists and return to the main menu
        """
        readstr.side_effect = ['1','1', 'y', 'NotJohn', "1000"]
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()

        
        self.assertEqual("MAIN MENU", ui.get_current_screen())


    
    @patch('src.user_input.read_string')
    def test_loan_item_success(self, readstr):
        """
        Test successfully loaning an item to a patron.
        The system should output a success message and return to the main menu.
        """
        readstr.side_effect = ['1','2', 'y', 'John Doe', '95', '2']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        
        john = ui._data_manager._patron_data[0]
        loan = john._loans[-1]
        self.assertEqual(loan._item._id, 2)
        self.assertEqual("MAIN MENU", ui.get_current_screen())

    
    @patch('src.user_input.read_string')
    def test_loan_item_fail(self, readstr):
        """
        Test failing to loan an item due to the patron being unable to borrow it.
        The system should output a failure message and return to the main menu.
        """
        readstr.side_effect = ['1','2', 'y', 'John Doe', '95', '100']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        
        john = ui._data_manager._patron_data[0]
        loan = john._loans[-1]
        self.assertNotEqual(loan._item._id, 2)
        self.assertEqual("MAIN MENU", ui.get_current_screen())


class TestReturnItem(unittest.TestCase):
    

    @patch('src.user_input.read_string')
    def test_return_item_patron_not_found(self, readstr):
        """
        Test attempting to return an item for a patron that does not exist.
        The system should output a message that no such patron exists and return to the main menu.
        """
        readstr.side_effect = ['2','NotJohn', "1000"]
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()

        self.assertEqual("MAIN MENU", ui.get_current_screen())

    @patch('src.user_input.read_string')
    def test_return_item_cant_find_item_then_success(self, readstr):
        """
        Test failing to find an item for return, then being able to provide the correct item,
        then successfully recording the return.
        The system should attempt multiple item searches and eventually return to the main menu after a successful return.
        """
        readstr.side_effect = ['2','John Doe', '95', '5', '6', '1']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        
        self.assertEqual("MAIN MENU", ui.get_current_screen())


class TestSearchForPatron(unittest.TestCase):
    

    @patch('src.user_input.read_string')
    def test_search_patron_by_name(self, readstr):
        """
        Test searching for a patron by name.
        The system should find and output details of the patrons matching the name.
        """
        readstr.side_effect = ['3','1', 'John Doe']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("SEARCH FOR PATRON", ui.get_current_screen())


        

    @patch('src.user_input.read_string')
    def test_search_patron_by_age(self, readstr):
        """
        Test searching for a patron by age.
        The system should find and output details of the patrons matching the age.
        """
        readstr.side_effect = ['3','2', '95']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("SEARCH FOR PATRON", ui.get_current_screen())
    
    @patch('src.user_input.read_string')
    def test_search_patron_by_age_not_found(self, readstr):
        """
        Test searching for a patron by an age that does not exist in the system.
        The system should output a message indicating no patrons were found.
        """
        readstr.side_effect = ['3','2', '1000']

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("SEARCH FOR PATRON", ui.get_current_screen())

    @patch('src.user_input.read_string')
    def test_search_patron_return(self, readstr):
        """
        Test returning to the main menu without searching for a patron.
        """
        readstr.side_effect = ['3','3']
        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("MAIN MENU", ui.get_current_screen())



class TestRegisterPatron(unittest.TestCase):

    @patch('src.user_input.read_string')
    def test_register_patron_success(self, readstr):
        """
        Test successfully registering a new patron.
        The system should add the patron to the patron data.
        """
        readstr.side_effect = ['4',"Jane Smith", '30']
        dm = DataManager()
        ui = BatUI(dm)
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual(dm._patron_data[-1]._name, "Jane Smith")
        self.assertEqual(dm._patron_data[-1]._age, 30)


class TestQuit(unittest.TestCase):

    @patch('src.user_input.read_string')
    def test_quit(self,readstr):
        """
        Test quitting the system.
        This is ok to run as a new class is created therefore no data gets changed 
        """
        readstr.side_effect = ['6']
        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("QUIT", ui.get_current_screen())



class TestCanAccessMakerspace(unittest.TestCase):
    
            
    @patch('src.user_input.read_string')
    def test_can_access_makerspace_patron_not_found(self, readstr):
        """
        Test attempting to access the makerspace with a non-existent patron.
        The system should output a message indicating that the patron was not found.
        """
        readstr.side_effect = ['5','NotJohn', "1000"]
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("MAIN MENU", ui.get_current_screen())
        
    @patch('src.user_input.read_string')
    def test_can_access_makerspace_fail(self, readstr):
        """
        Test attempting to access the makerspace for a patron who is not allowed.
        The system should output a message indicating the patron cannot access the makerspace.
        """
        readstr.side_effect = ['5','John Doe', '95']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("MAIN MENU", ui.get_current_screen())


    @patch('src.user_input.read_string')
    def test_can_access_makerspace_success(self, readstr):
        """
        Test successfully accessing the makerspace for a patron who is allowed.
        The system should output a message indicating the patron can use the makerspace then return to the main menu.
        """
        readstr.side_effect = ['5','Jane Smith', '23']
        

        ui = BatUI(DataManager())
        ui.run_current_screen()
        ui.run_current_screen()
        self.assertEqual("MAIN MENU", ui.get_current_screen())

        
