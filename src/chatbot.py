"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Benjamin Omoregie
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:



def get_account() -> int:
    """
    args(): no parameters.

    return(int): return the users_selection if it an integer.

    raises:
        Exception: if Account number does not exist.
        valueerror: if Acount number is not a whole number
        """

    #if  user_selction is valid.
    try:
        user_selection = input('Please enter your account number: ')
        account_number = int(user_selection)
    except Exception:
        raise ValueError('Account Number must be a whole number.')
    if account_number not in ACCOUNTS:
        raise ValueError('Acount Number Does not Exsist.')
    return account_number #returns account number if it in ACCOUNTS.

def get_amount() ->float:
    """
    args(): no parameters.

    return(float): returns a user_selection if its valid.

    raises:
        valueError: if user_selection is not numeric. 
        Exception: if user_selection is zero or negative number.
        """
    valid = True
    while valid:
        try:
            user_selection = input('Enter the transaction amount: ')
            amount = float(user_selection)
        except Exception:
            raise ValueError('invalid amount. Amount must be numeric.')
        
        if amount <= 0:
            raise ValueError('Invalid amount. please enter a positive number.')
        return amount
    


        
def get_balance(account: int) -> str:
    """
    args:
    amount(int): the account number must be  an integer.

    return(str): returns a string message that includes account number and balance.

    raises:
        Exception: if account number does not exisit.
    """
    if account not in ACCOUNTS:
        raise ValueError('Account number does not exist.')
    balance = ACCOUNTS[account]['balance']
    return f'Your current balance for account {account} is ${balance:.2f}.'
    


def make_deposit(account: int, amount: float) -> str:
     """
    args:
    account(int): the account number must be  an integer.
    amount(float): the amount of deposit must be a float.

    return(str): returns a string message that includes account number and balance.

    raises:
        Exception: if account number does not exist.
        Value error: if amount is negative.
    """
     if account not in ACCOUNTS:
         raise Exception('Account number does not exisit.')
     if amount <= 0:
        raise ValueError('Invalid amount.amount must be positive.')
     
     balance = ACCOUNTS[account]['balance']
     account_balance = balance + amount
     ACCOUNTS[account]['balance'] = account_balance
     return f'You have made a deposit of ${amount:.2f} to account {account}.'

def user_selection() -> str:
     """
    args(): no parameters.

    return(): returns a user_selection if its in Valid_Task.

    raises:
        valueError: raises ValueError if selection is not in Valid_Tasks. 
     """
    
     user_selection = input('what would you like to do (balance/deposit/exit)? ').lower()
     if user_selection not in VALID_TASKS:
         raise ValueError('Invalid task. Please choose balance, deposit, or exit.')   
      
     return user_selection

           
     




         
    
            




## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION

def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
    get_account()
    get_amount()
    get_balance()
    make_deposit()
    user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:
            selection = user_selection()
            if selection != "exit":
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:
                        account = get_account()
                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:
                        balance = get_balance(account)
                        print(balance)
                else:
                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:
                            amount = get_amount()
                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING TH
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:
                    result = make_deposit(account, amount)
                    print(result)
            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")

if __name__ == "__main__":
    chatbot()
