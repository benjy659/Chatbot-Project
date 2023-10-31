"""
Description: For testing chatbot application.
Author: Benjamin Omoregie
Date: 30/10/23
Usage: The chatbot Alows users perform balance enquire andd make deposit to thier accounts.
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account,VALID_TASKS,ACCOUNTS,get_amount,get_balance,make_deposit

class chatbotTests(unittest.TestCase):
    def test_get_account_valid(self):
     #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for valid account number.
        # values that are prompted for in the function:
            mock_input.side_effect = ['123456']
            expected = 123456
            #Act
            actual = get_account()
            #Assert
            self.assertEqual(expected, actual)

    def test_get_account_invalid(self):
        #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for non numeric number.
            mock_input.side_effect = ['adsr']
            expected = 'Account Number must be a whole number.'
            #Act and Asssert
            #assertRaies(ValueError) <-- because function raises
            # ValueError when an invalid acount number is provided.
            with self.assertRaises(ValueError) as context:
                get_account()
            self.assertEqual(str(context.exception), expected)
    
    def test_get_account_invalid(self):
        #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for non numeric number.
            mock_input.side_effect = ['1122233']
            expected = 'Acount Number Does not Exsist.'
            #Act and Asssert
            #assertRaies(ValueError) <-- because function raises
            # ValueError when an invalid acount number is provided.
            with self.assertRaises(Exception) as context:
                get_account()
            self.assertEqual(str(context.exception), expected)
    
    
    def test_get_amount_valid(self):
     #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for valid account amount
        # values that are prompted for in the function:
            mock_input.side_effect = ['500.1']
            expected = 500.1
            #Act
            actual = get_amount()
            #Assert
            self.assertEqual(expected, actual)

    def test_get_amount_nonnumeric(self):
        #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for invalid amount.
            mock_input.side_effect = ['ab']
            expected = 'invalid amount. amount must be numeric.'
            #Act and Asssert
            #assertRaies(ValueError) <-- because function raises
            with self.assertRaises(ValueError) as context:
                get_amount()
            self.assertEqual(str(context.exception), expected)

    def test_get_amount_invalid(self):
        #builtins.input <-- allows us to mock input
        with patch('builtins.input') as mock_input:
        #Arrange
        #the side_effect list below 'mocks' input for zero or negative number.
            mock_input.side_effect = ['0']
            expected = 'Invalid amount. please enter a positive number.'
            #Act and Asssert
            #assertRaies(ValueError) <-- because function raises
            with self.assertRaises(Exception) as context:
                get_amount()
            self.assertEqual(str(context.exception), expected)

    def test_get_balance_correct_account(self):
        #Arrange
        account = 123456
        expected = f'Your current balance for account 123456 is $1000.00.'
        #Act
        result = get_balance(account)
        #Assert
        self.assertEqual(result, expected)
    
    def test_get_balance_invalid_account(self):
        #Arrange
        account = 112233
        expected = 'Account number does not exist.'
        #Act and Assert
        with self.assertRaises(Exception) as context:
            get_balance(account)
        self.assertEqual(str(context.exception), expected)

    def test_make_deposit_balance_updated(self):
        #Arrange
        account_number = 123456
        ACCOUNTS[account_number]['balance'] = 1000.0
        deposit_amount = 1500.01
        expected = 1000.0 + deposit_amount
        #Act
        actual = make_deposit(account_number, deposit_amount)
        #Assert
        self.assertEqual(ACCOUNTS[account_number]['balance'], expected)
    def test_make_deposit_correct_value_returned(self):
        #Arrange
        account_number = 123456
        ACCOUNTS[account_number]['balance'] = 1000.0
        deposit_amount = 1500.01
        expected = 'You have made a deposit of $1500.01 to account 123456.'
        #Act
        actual = make_deposit(account_number, deposit_amount)
        #Assert
        self.assertEqual(actual, expected)
    def test_make_deposit_invalid_account(self):
        #Arrange
        account_number = 112233
        deposit_amount = 1500.01
        expected = 'Account number does not exisit.'
        #Act
        #assert
        with self.assertRaises(Exception) as context:
                make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), expected)
    
    def test_make_deposit_invalid_amount(self):
        #Arrange
        account_number = 123456
        deposit_amount = -50.01
        expected = 'Invalid amount.amount must be positive.'
        #Act
        #assert
        with self.assertRaises(ValueError) as context:
                make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), expected)


        

