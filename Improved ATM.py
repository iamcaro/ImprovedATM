import datetime

timeStamp = datetime.datetime.now()

import random
 
def generationAccountNumber():    
    return random.randrange(1111111111,9999999999)

database = {} 

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
    password = input("What is your password? \n")    

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)
                   
    print("Invalid account or password")
    attempt = int(input("(1) Try again, (2) Exit \n"))
    if(attempt == 1):
        login()
    else:
        init()


def register():

    print("***** Please register *****")

    email = input("What is your email address? \n")
    first_name  = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")
    currentBalance = 0

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password, currentBalance]

    print("Your account has been created")
    print(" ============================")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" ============================")

    login()

def bankOperation(user):

    print("=========================== \n")
    print(timeStamp.strftime("%x %X"))
    print()

    print("Welcome %s %s! \n" % (user[0], user[1]))

  
    while True:
        selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

        if(selectedOption == 1):
            depositOperation(user)

        elif(selectedOption == 2):
            withdrawalOperation(user)

        elif(selectedOption == 3):
            logout()

        elif(selectedOption == 4):
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