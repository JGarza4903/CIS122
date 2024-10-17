#******************************************************************************
# Author:           Joshua Garza
# Lab:              Practice #4
# Date:             10/14/2024
# Description:      program that propmpts user for amount of cents as an 
#                   integer and returns the exact amount in change.  
# Input:            change: int
# Output:           Number of dollars, dimes, nickels and pennies.
# Sources:          Practice 4 specifications.
#                   -Have a main() function.
#                   -Have a function for every input, process (calculation),
#                       and output. 
#                   -Include a function comment in each function with a 
#                       description, parameters, and return changeTypes.  
#                   -Declare result variables in functions. 
#                   -Make sure that you are doing the correct singular/plural 
#                       output for each dollar/coin type.  
#                   -Include at least 1 selection.            
#******************************************************************************

#******************************************************************************
# Sample Run:
#
#     Welcome to the virtual change converter. 
#
#  We take your pennies and return dollars and cents.
#        Enter amount as a whole number.
#            Ex: 1542 = $15.42
#
# How much would you like to convert? 1542
#
# Your amount of $15.42 in change is:
#
#   Dollars: 15
#   Quarters: 1
#   Dimes: 1
#   Nickels: 1
#   Pennies: 2
#
# Thanks for using the virtual change machine!
#******************************************************************************

def main():
    """ 
    Program will prompt user to enter amount (USD) as a whole number and return 
    the exact amount of change.
    :param: none
    :return: none
    """ 
    # Initialize variables
    originalAmount = 0
    cents = 0
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0 
    pennies = 0

    # Constant variable values
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5

    # Greet User and inorm them the purpose of this program. 
    printGreeting()

    # Prompt user for amount to convert and store it in an OG variable.
    originalAmount = getAmount()

    # Calculate the amount of dollars
    dollars = calculateDollars(originalAmount)

    # Update the remaining change and change variable to cents
    cents = updateChange(originalAmount, DOLLAR)

    # Calculate the amount of quarters
    quarters = calculateQuarters(cents)

    # Update the remaining change
    cents = updateChange(cents, QUARTER)

    # Calculate the amount of dimes
    dimes = calculateDimes(cents)

    # Update the remaining change
    cents = updateChange(cents, DIME)

    # Calculate the amount of nickels
    nickels = calculateNickels(cents)

    # Update the remaining change to pennies.
    pennies = updateChange(cents, NICKEL)

    # Print results to the user
    printResults(originalAmount, dollars, quarters, dimes, nickels, pennies)

    # Say goodbye to the user
    printGoodbye()

def printGreeting():
    """
    Welcomes the user and informs them the purpose of this program.
    :param: none
    :return: none
    """ 
    print("Hello,\n")
    print("     Welcome to the virtual change machine.\n")
    print("We take your pennies and return dollars and cents.") 
    print("       Enter amount as a whole number.")
    print("           Ex: 1542 = $15.42\n")

def getAmount():
    """
    Prompts the user to enter a $ changeType as an whole integer.
        Ex: $15.42 = 1542
    :param: none
    :return: cents: int, amount of total cents
    """
    cents = 0
    cents = int(input("How much would you like to convert? "))
    return cents

def calculateDollars(cents):
    """ 
    Calculates amount of dollars by floor division of 100 on cents integer.
    :param: cents: int, amount of total cents
    :return: dollars: int, amount of dollars
    """ 
    dollars = 0
    dollars = cents // 100
    return dollars

def calculateQuarters(cents):
    """
    Calculates amount of quarters by floor division of 25 on cents integer.
    :param: cents: int, amount of total cents
    :return: quarters: int, amount of quarters
    """
    quarters = 0
    quarters = cents // 25
    return quarters

def calculateDimes(cents):
    """
    Calculates amount of dimes by floor division of 5 on cents integer.
    :param: cents: int, amount of total cents
    :return: dimes: int, amount of dimes
    """
    dimes = 0
    dimes = cents // 10
    return dimes

def calculateNickels(cents):
    """
    Calculates amount of nickels by floor division of 10 on cents integer.
    :param: cents: int, amount of total cents
    :return: nickels: int, amount of nickels
    """
    nickels = 0
    nickels = cents // 5
    return nickels

def updateChange(cents, changeType):
    """ 
    Calculates the remaining change based on the change-type being entered
    :param: cents: int, amount of total cents
    :param: changeType: int, value each type of change has.
    :return: newChange: int, updated value of remaining change.
    """ 
    newChange = 0

    if changeType == 100:
        newChange = cents % changeType 
    elif changeType == 25:
        newChange = cents % changeType 
    elif changeType == 10:
        newChange = cents % changeType
    elif changeType == 5:
        newChange = cents % changeType
    return newChange

def printResults(originalAmount, dollars, quarters, dimes, nickels, pennies):
    """
    prints results from calculations, and formats the original amount.
    :param: originalAmount: int, user input of integer number
    :param: dollars: int, number of dollars
    :param: quarters: int, number of quarters
    :param: dimes: int, number of dimes
    :param: nickels: int, number of nickels
    :param: pennies: int, number of pennies
    :return: results: string, results of calculation
    """ 
    # Converts the original amount to show formatted as $xx.xx 
    formattedAmount = originalAmount / 100

    results = print("""
    Your amount of ${:,.2f} in change is:

        Dollars: {:,}
        Quarters: {}
        Dimes: {}
        Nickels: {}
        Pennies: {}
    """.format(formattedAmount, dollars, quarters, dimes, nickels, pennies)) 

    return results

def printGoodbye():
    """ 
    Informs the user the program is finished.
    :param: none
    :return: message: str, saying goodbye
    """ 
    print("Thanks for using the virtual change machine!\n")


if __name__ == "__main__":
    main()