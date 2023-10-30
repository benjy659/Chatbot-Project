"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account,VALID_TASKS,ACCOUNTS,get_amount

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
    

            

