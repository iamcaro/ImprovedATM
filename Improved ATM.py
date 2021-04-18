import datetime

timeStamp = datetime.datetime.now()

import random
import validation
import database
import os
from getpass import getpass

auth_session_path = "data/auth_session/"

def generationAccountNumber():    
    return random.randrange(1111111111,9999999999)


def init():
    
    print()
    print("******* Welcome to Bank Python *******")

    haveAccount = int(input("Do you have an account with us? 1 (yes), 2 (no) \n"))
        
    if(haveAccount == 1):
        login()
            
    elif(haveAccount == 2):
        register()

    else:
        print("You have selected an invalid option")
        init()


def login():
    
    print()
    print("*****Login to your account***** \n")

    accountNumberFromUser = int(input("What is your account number? \n"))

    is_valid_account_number = validation.account_number_validation(accountNumberFromUser)

    if is_valid_account_number:

        password = getpass("What is your password? \n")    

        user = database.authenticated_user(accountNumberFromUser, password)

        if user:
            
            create_auth_session(accountNumberFromUser)
            
            bankOperation(accountNumberFromUser, user)
                   
        print("Invalid account or password")

    else:
        print("Account number invalid")    

    attempt = int(input("(1) Try again, (2) Exit \n"))
    
    if(attempt == 1):
        login()
    
    else:
        init()


def create_auth_session(user_account_number):
    try:

        f = open(auth_session_path + str(user_account_number) + ".txt", "x")

    except FileExistsError:
        # Ignore error if file exists.
        pass

    else:
        f.close()

def delete_auth_session(user_account_number):

    is_delete_successful = False

    if os.path.exists(auth_session_path + str(user_account_number) + ".txt"):

        try:

            os.remove(auth_session_path + str(user_account_number) + ".txt")
            is_delete_successful = True

        except FileNotFoundError:

            print("File not found")

        finally:

            return is_delete_successful


def register():

    print("***** Please register *****")

    email = input("What is your email address? \n")
    first_name  = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = getpass("Create a password for yourself \n")
    
    accountNumber = generationAccountNumber()

    is_user_created = database.create(accountNumber, first_name, last_name, email, password)

    if is_user_created:

        print("Your account has been created")
        print(" ============================")
        print("Your account number is: %d" % accountNumber)
        print("Make sure you keep it safe")
        print(" ============================")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bankOperation(accountNumber, user):

    print("=========================== \n")
    print(timeStamp.strftime("%x %X"))
    print()

    print("Welcome %s %s! \n" % (user[0], user[1]))

    # Converting the balance to an integer to do math on it.
    user[4] = int(user[4])

    while True:
        selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

        if(selectedOption == 1):
            depositOperation(user)

        elif(selectedOption == 2):
            withdrawalOperation(user)

        elif(selectedOption == 3):
            database.save(accountNumber, user)
            delete_auth_session(accountNumber)
            logout()

        elif(selectedOption == 4):
            database.save(accountNumber, user)
            delete_auth_session(accountNumber)
            exit()

        else:
            print("Invalid option selected")
        

def depositOperation(user):
    print("You have selected the Deposit option")

    amountD = int(input("How much would you like to deposit? \n"))
    print("%d has been deposited to your account \n" % amountD)

    user[4] += amountD
    print("Your current balance is %d" % user[4])

def withdrawalOperation(user):
    print("You have selected the Withdrawal option")

    amountW = int(input("How much would you like to withdraw? \n"))
    
    if(amountW > user[4]):
        print("Sorry. Insufficient funds")
    
    else:
        print("Please retrieve your money \n")
        user[4] -= amountW
        print("Your current balance is %d" % user[4])


def logout():
    login()


def exit():
    print("Thank you for your business. Goodbye! \n")
    init()


#### ACTUAL BANKKING SYSTEM ####

init()