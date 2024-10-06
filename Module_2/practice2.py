#******************************************************************************
# Author:           Joshua Garza
# Lab:              Practice #2
# Date:             10/2/2024
# Description:      Example: This program prompts a user for their vehicles MPG 
#                   and gas price to inform the financial cost it would take to 
#                   travel at multiple distances.
# Input:            Car's mpg: float, 
#                   gas_price_per_gallon: float
# Output:           Gas cost for driving 20, 75 and 500 miles
# Sources:          Practice 2 specifications.
#                   Prompt a user to input two float numbers: 
#                      one for a car's mpg (miles per gallon)
#                      one for the gas price per gallon
#                   Output the gas cost for 20 miles, 75 miles, and 500 miles
#                   
#******************************************************************************

#******************************************************************************
# Sample Run:

# Hello!

# This program calculates the cost to travel based on your vehicles mpg and gas 
# prices.

# Enter your vehicles estimated mpg (Miles per Gallon): 20

# Enter the cost of gas per gallon: 2.89

# You've entered:       
#   2.89 as the cost per gallon
#   20.00 as the vehicles MPG.

# Based on the information you've provided, here is the cost of traveling:
#     20 Miles:    $2.89
#     75 Miles:    $10.84
#     500 Miles:   $72.25

# Safe Travels!
#******************************************************************************

# Initiate constant variables, the distances to check.
DISTANCE_1 = 20
DISTANCE_2 = 75      
DISTANCE_3 = 500

# Greet and inform user the purpose of this program.
print('''Hello!

This program calculates the cost to travel based on your vehicles mpg and 
gas prices.
''')

# Prompt user to enter mpg and cost of gas and store each into variables
mpg = float(input("Enter your vehicles Miles per Gallon: "))
cost_per_gallon = float(input("What is your current gas price? (Ex: 2.89): "))

# Echo back to user their entries.
print('''
You've entered:
    {:.2f} as the cost per gallon
    {:.2f} as the vehicles MPG 
    '''.format(cost_per_gallon,mpg))

# Calculate how many gallons were consumed during travel for each distance
# 1. Use integer flooring on constants to determine full miles
# 2. Use Modolus on constants to find remainder
# 3. Divide the remainder by the vehicles MPG and add to miles traveled. 

# Distance 1
distance_1_miles = DISTANCE_1 // mpg
distance_1_remainder = DISTANCE_1 % (distance_1_miles * mpg)
distance_1_gallons_used = (distance_1_miles + (distance_1_remainder / mpg))

# Distance 2
distance_2_miles = DISTANCE_2 // mpg
distance_2_remainder = DISTANCE_2 % (distance_2_miles * mpg)
distance_2_gallons_used = (distance_2_miles + (distance_2_remainder / mpg))

# Distance 3
distance_3_miles = DISTANCE_3 // mpg
distance_3_remainder = DISTANCE_3 % (distance_3_miles * mpg)
distance_3_gallons_used = (distance_3_miles + (distance_3_remainder / mpg))


# Calculate total cost of gas used based on distances driven (our constants).
distance_1_cost = distance_1_gallons_used * cost_per_gallon
distance_2_cost = distance_2_gallons_used * cost_per_gallon
distance_3_cost = distance_3_gallons_used * cost_per_gallon


# Inform user of their cost and provide cost examples of 3 different distances.
print('''Based on the information you've provided, here is the cost of traveling:
    20 Miles:       ${:.2f}
    75 Miles:       ${:.2f}
    500 Miles:      ${:.2f}
'''
.format(distance_1_cost, distance_2_cost, distance_3_cost))

# Wish users a safe travel
print("Safe Travels!")