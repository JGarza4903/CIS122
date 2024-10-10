#******************************************************************************
# Author:           Joshua Garza
# Lab:              Lab 3
# Date:             10/10/2024
# Description:      Adding items into existing Inventory and calculating total
#                   inventory cost.
# Input:            User Name: string
#                   Item Quantity: integer           
# Output:           Updated inventory levels and overhead cost
# Sources:          Lab 3 specifications:
#                   Course Material
#******************************************************************************

#******************************************************************************
# Sample Run:

# Hello, Welcome to the Bike Stop Inventory App!

# May I please get your name? Joshua

# Hi Joshua,

# Our current inventory level for recycled bikes is:

#     Total Stock: 10 Bikes
#     Total Stock($): $995.50

# How many bikes would you like to add to inventory? 5

# You've added 5 bikes, your new inventory level is:

#     Total Stock: 15 Bikes
#     Total Stock($): $1,499.50

# Thanks Joshua for using the Bike Stop Inventory App!


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
    qtyToAdd = 0
    totalInventoryCost = 0.0
    UNIT_PRICE = 99.95

    # Greet the user and ask for their name.
    name = printGreeting()

    # inform user of current inventory level.
    totalInventoryCost = calculateStockLevel(bikesInStock, UNIT_PRICE)

    # Prompt the user to select the number of bikes to enter in inventory.
    qtyToAdd = addItem()
    
    # Add qty entered by user into the total amount of bikes in inventory
    bikesInStock = updateStock(qtyToAdd, bikesInStock)

    # Echo back their selection and inform user of updated stock levels.
    totalInventoryCost = calculateStockLevel(bikesInStock, UNIT_PRICE)

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
    print('\nHello! Welcome to the Bike Stop Inventory App\n')
    name = input("May I please get your name? ")
    print("\nHi {},\n".format(name))
    print("Our current inventory level for recycled bikes is:")
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

    return totalInventoryCost

def addItem():
    """
    Adds the quantity entered by user to the total # of bikes in inventory.
    :param: none
    :return: qtyToAdd: int, number of bikes being added to inventory
    """
    qtyToAdd = 0
    qtyToAdd = int(input("How many bikes would you like to add to stock? "))
    return qtyToAdd

def updateStock(qtyToAdd, stockLevel):
    """ 
    Adds the qty entered by user into the bike inventory and echoes back 
    selection to user.
    :param: qtyToAdd: int, number to add into stock 
    :param: stockLevel: int, current stock level
    :return: bikesInStock: int, calculated total of bikes in stock.
    """
    bikesInStock = 0
    bikesInStock = qtyToAdd + stockLevel
    print("""\nYou added {} bikes into inventory. New inventory level is:"""
    .format(qtyToAdd))

    return bikesInStock

def printGoodbye(name):
    """ 
    Informs user the prgram has finished running
    :param: name: string, the users name
    :return: none
    """ 
    print('Thanks {} for using the Bike Stop Inventory App'.format(name))

# Run main program 
if __name__ == "__main__":
    main()