#******************************************************************************
# Author:           Joshua Garza
# Lab:              Lab 4
# Date:             10/17/2024
# Description:      Adding items into existing Inventory and calculating total
#                   inventory cost.
# Input:            User Name: string
#                   Item Quantity: integer           
# Output:           Updated inventory levels and overhead cost
# Sources:          Lab 4 specifications:
#                   -Add at least two decision structures (If statements), to 
#                    your program.
#                       -One decision structure with multiple "elif" clauses is 
#                        considered 1 decision structure.
#******************************************************************************
#******************************************************************************
# Sample Run 1:
#
# Hello, Welcome to the Bike Stop Inventory App!
#
# May I please get your name? Joshua
#
# Hi Joshua,
#
# Select from the options below.
#
# Main Menu - 
#   1. Check Inventory
#   2. Add Inventory
#   3. Remove Inventory
#   4. Quit Program
#
# What would you like to do? (please select a number): 1
#
# Our current inventory level for recycled bikes is:
#
#     Total Stock: 10 Bikes
#     Total Stock($): $995.50
#
# Thanks Joshua for using the Bike Stop Inventory App!
#
#******************************************************************************
# Sample Run 2:
#
# Hello, Welcome to the Bike Stop Inventory App!
#
# May I please get your name? Joshua
#
# Hi Joshua,
#
# Select from the options below.
#
# # Main Menu -Select from the options below. 
#   1. Check Inventory
#   2. Add Inventory
#   3. Remove Inventory
#   4. Quit Program
#
# What would you like to do? (please select a number): 2
#
# How many bikes would you like to add? 5
#
# You've added 5 bikes, your new inventory level is:
#
#     Total Stock: 15 Bikes
#     Total Stock($): $1,499.50
#
# Thanks Joshua for using the Bike Stop Inventory App!
#
#******************************************************************************
# Sample Run 3:
#
# Hello, Welcome to the Bike Stop Inventory App!
#
# May I please get your name? Joshua
#
# Hi Joshua,
#
# Select from the options below.
#
# Main Menu -Select from the options below. 
#   1. Check Inventory
#   2. Add Inventory
#   3. Remove Inventory
#   4. Quit Program
#
# What would you like to do? (please select a number): 3
#
# How many bikes would you like to remove? 10
#
# You've removed 10 bikes, your new inventory level is:
#
#     Total Stock: 5 Bikes
#     Total Stock($): $499.50
#
# Thanks Joshua for using the Bike Stop Inventory App!
#
#******************************************************************************
# Sample Run 4:
#
# Hello, Welcome to the Bike Stop Inventory App!
#
# May I please get your name? Joshua
#
# Hi Joshua,
#
# Select from the options below.
#
#  Main Menu -Select from the options below. 
#   1. Check Inventory
#   2. Add Inventory
#   3. Remove Inventory
#   4. Quit Program
#
# What would you like to do? (please select a number): 4
#
# Thanks Joshua for using the Bike Stop Inventory App!
#
#******************************************************************************

def main():
    """
    Program that adds items into existing Inventory and calculates the total
    inventory value.
    :param: none
    :return: bikesInStock: int, total number of bikes inventoried
    :return: totalInventoryCost: float, total amount of inventory value
    """   
    # Initiate variables and constants
    bikesInStock = 10
    UNIT_PRICE = 99.95

    # Greet the user and ask for their name.
    name = printGreeting()

    # Ask user what they would like to do 
    userChoice = menuChoices()

    # Display results based on users input.
    menuResults(userChoice, bikesInStock, UNIT_PRICE, name)

    # Inform the user the program has finished running. 
    printGoodbye(name)

def printGreeting():
    """ 
    Greets user and asks for name, informs user ots purpose and current 
    inventory levels.
    :param: none
    :return: name: string, the user's name.
    """ 
    name = ""
    print('\nHello!\n\nWelcome to the Bike Stop Inventory App\n')
    name = input("May I please get your name? ")
    print("\nHi {},\n".format(name))

    return name

def calculateStockLevel(bikesInStock, UNIT_PRICE):
    """ 
    Calculates the stock value by multiplying # of bikes by the unit cost 
    and prints out the results.
    :param: bikesInStock: int, number of bikes in inventory.
    :param: UNIT_PRICE: float, price per unit
    :return: totalInventoryCost: float, value of bikes in inventory.
    """ 
    totalInventoryCost = 0.0
    totalInventoryCost = bikesInStock * UNIT_PRICE
    print("""
        Total Stock:        {} Bikes
        Total Stock($):     ${:,.2f}
        """.format(bikesInStock, totalInventoryCost))

def menuChoices():
    """ 
    Prompts a menu of 4 choices for user to select indicated by a number.
    :param: none
    :return: selection: int, users selection as a number
    """ 
    selection = 0
    print("""Select from the options below.

    Main Menu - 
        1. Check Inventory
        2. Add Inventory
        3. Remove Inventory
        4. Quit Program\n""")

    text = "What would you like to do? (please select a number): "
    selection = int(input(text))

    return selection

def menuResults(selection, bikesInStock, UNIT_PRICE, name):
    """
    Perform action based on users choice.
    :param: selection: int, users selection of menu options.
    :return: results: 
    """
    if selection == 1:
        # Echo back their selection and inform user of updated stock levels
        print("\nYour current inventory is:")
        calculateStockLevel(bikesInStock, UNIT_PRICE)
    elif selection == 2:
        # Prompt user to enter # of bikes to going to inventory.
        qtyToAdd = addItem()
        bikesInStock = updateStock(qtyToAdd, bikesInStock)
        # Echo back their selection and inform user of updated stock levels
        calculateStockLevel(bikesInStock, UNIT_PRICE)
    elif selection == 3:
        # Prompt user to enter # of bikes to removing frominventory.
        qtyToRemove = removeItem()
        bikesInStock = updateStock(qtyToRemove, bikesInStock)
        # Echo back their selection and inform user of updated stock levels
        calculateStockLevel(bikesInStock, UNIT_PRICE)
    elif selection == 4:
        pass
    else:
        print("Invalid. Please select a number or enter '4' to exit.")
        new_selection = int(input("New Choice:"))
        menuResults(new_selection)

def addItem():
    """
    Adds the quantity entered by user to the total # of bikes in inventory.
    :param: none
    :return: qtyToAdd: int, number of bikes being added to inventory
    """
    qtyToAdd = 0
    qtyToAdd = int(input("\nHow many bikes would you like to add to stock? "))

    return qtyToAdd

def updateStock(qtyToCalculate, stockLevel):
    """ 
    Adds the qty entered by user into the bike inventory and echoes back 
    selection to user.
    :param: qtyToAdd: int, number to add into stock 
    :param: stockLevel: int, current stock level
    :return: bikesInStock: int, calculated total of bikes in stock.
    """
    # Determine if calculation is adding or subtracting.
    if qtyToCalculate > 0:
        text = "added"
    else:
        text = "removed"
    
    # store number as absolute just for print message. 
    absolute_value = abs(qtyToCalculate)

    bikesInStock = 0
    bikesInStock = qtyToCalculate + stockLevel
    print("""\nYou {} {} bikes into inventory. New inventory level is:"""
    .format(text, absolute_value))

    return bikesInStock

def printGoodbye(name):
    """ 
    Informs user the prgram has finished running
    :param: name: string, the users name
    :return: none
    """ 
    print('\nThanks {} for using the Bike Stop Inventory App\n'.format(name))

def removeItem():
    """
    Removes the qty entered by user from the total # of bikes in inventory.
    :param: none
    :return: qtyToRemove: int, number of bikes being removed from inventory
    """
    qtyToRemove = 0
    text="\nHow many bikes would you like to remove from stock?: "
    qtyToRemove = int(input(text))

    # transform int to a negative to avoid changing "updateStock" function.
    qtyToRemove = qtyToRemove * -1

    return qtyToRemove

# Run main program 
if __name__ == "__main__":
    main()