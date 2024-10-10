#******************************************************************************
# Author:           Joshua Garza
# Lab:              Lab 2
# Date:             9/25/2024
# Description:      Adding items into existing Inventory and calculating total
#                   inventory cost.
# Input:            Item Name: string
#                   Item Quantity: integer           
# Output:           Updated inventory levels and overhead cost
# Sources:          Lab 2 specifications:
#                   Course Material
#******************************************************************************

#******************************************************************************
# Sample Run:

# Hello, Welcome to the Bike Stop Inventory App!

# May I please get your name? Josh

# Hi Josh,

# Our current inventory level for recycled bikes is:

#     Total Stock: 10 Bikes
#     Total Stock($): $995.50

# How many bikes would you like to add to inventory? 5

# You've added 5 bikes, your new inventory level is:

#     Total Stock: 15 Bikes
#     Total Stock($): $1,499.50

# Thank you for using the Bike Stop Inventory App!

#******************************************************************************

# Initiate variables and constants
name =''
bikes = 10
quantity_to_add = 0
UNIT_PRICE = 99.95

# Greet the user and ask for their name.
print('\nHello! Welcome to the Bike Stop Inventory App\n')
name = input("May I please get your name? ")

# inform them of current inventory level.
print('''
Hi {},

Our current inventory level for recycled bikes are:

    Total Stock:        {} Bikes
    Total Stock($):     ${:,.2f}
    '''.format(name, bikes, UNIT_PRICE * bikes))

# Prompt the user to select the number of bikes entering into inventory.
quantity_to_add = int(input("How many bikes would you like to add to stock? "))

# Add quantity to existing number in stock and calculate new associated cost
bikes = bikes + quantity_to_add
total_inventory_cost = UNIT_PRICE * bikes

# Echo back their selection and inform user of updated stock levels.
print('''
You've added {} bikes, your new inventory level is:

    Total Stock:        {} Bikes
    Total Stock($):     ${:,.2f}
    '''.format(quantity_to_add, bikes, total_inventory_cost))

# Inform the user the program has finished running. 
print('Thank you for using the Bike Stop Inventory App')