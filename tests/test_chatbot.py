"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account,VALID_TASKS,ACCOUNTS

class chatbotTests(unittest.TestCase):
    def test_get_account_valid(self):
     #builtins.input <-- allows us to mock input
        #builtins.print <-- would allow us to mock print
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
            

