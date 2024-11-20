import unittest
from unittest import mock


from src.bat_ui import BatUI
from src.data_mgmt import DataManager

class TestMainMenu(unittest.TestCase):
    @mock.patch('src.user_input.read_string')
    def test_loan_screen(self, readstr):
        """
        Test that selecting option '1' from the main menu navigates to the 'LOAN ITEM' screen.
        Mocks user input to simulate selecting the loan item option.
        """
        readstr.return_value = '1'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("LOAN ITEM", ui.get_current_screen())

    def test_main_menu(self):
        """
        Test that the default screen on application start is the 'MAIN MENU'.
        """
        ui = BatUI(DataManager())
        self.assertEqual("MAIN MENU", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_return_screen(self, readstr):
        """
        Test that selecting option '2' from the main menu navigates to the 'RETURN ITEM' screen.
        Mocks user input to simulate selecting the return item option.
        """
        readstr.return_value = '2'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("RETURN ITEM", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_search_for_patron_screen(self, readstr):
        """
        Test that selecting option '3' from the main menu navigates to the 'SEARCH FOR PATRON' screen.
        Mocks user input to simulate selecting the search for patron option.
        """
        readstr.return_value = '3'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("SEARCH FOR PATRON", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_register_patron_screen(self, readstr):
        """
        Test that selecting option '4' from the main menu navigates to the 'REGISTER PATRON' screen.
        Mocks user input to simulate selecting the register patron option.
        """
        readstr.return_value = '4'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("REGISTER PATRON", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_access_makerspace_screen(self, readstr):
        """
        Test that selecting option '5' from the main menu navigates to the 'ACCESS MAKERSPACE' screen.
        Mocks user input to simulate selecting the access makerspace option.
        """
        readstr.return_value = '5'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("ACCESS MAKERSPACE", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_quit_screen(self, readstr):
        """
        Test that selecting option '6' from the main menu navigates to the 'QUIT' screen.
        Mocks user input to simulate selecting the quit option.
        """
        readstr.return_value = '6'
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("QUIT", ui.get_current_screen())

    @mock.patch('src.user_input.read_string')
    def test_out_of_range(self, readstr):
        """
        Test that invalid or out-of-range options from the main menu result in staying on the main menu
        until a valid option is selected.
        Mocks user input to simulate out-of-range selections.
        """
        readstr.side_effect = ['8', '-1', '1.5', 'abc', '3']
        ui = BatUI(DataManager())
        ui.run_current_screen()
        self.assertEqual("SEARCH FOR PATRON", ui.get_current_screen())
