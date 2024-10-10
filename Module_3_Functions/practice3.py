#******************************************************************************
# Author:           Joshua Garza
# Lab:              Practice #3
# Date:             10/10/2024
# Description:      Example: program is a gumball estimator that prompts user 
#                   for the dimensions of a cylinder and then calculates the 
#                   number of 1" gumballs that will fit inside
# Input:            daimeter: float, 
#                   height: float
# Output:           Number of 1" gumballs it takes to fill the jar.
# Sources:          Practice 3 specifications.
#                   Create a main() function.
#                   Create a function for every input, process (calculation), 
#                       and output. 
#                   Declare result variables in functions. Do not return an 
#                       equation. Assign the result variable(s) the equation 
#                       result, the return the result variable(s).
#                   Include a function comment in each function with a 
#                       description, parameters, and return value. Use """ """ 
#                       to create your comment, take a look at the 
#                       lab3example.pdf for an example.                  
#******************************************************************************

#******************************************************************************
# Sample Run:

# Gumball Estimator!
# Enter the dimensions of a cylinder jar and I will
# tell you how many gumballs it will take to fill!

# Enter cylinder diameter (inches): 7
# Enter cylinder height (inches): 10

# The jar will hold 477 gumballs!

# Goodbye!
#******************************************************************************

def main():
    """
    The program is a gumball estimator that prompts a user for the dimensions 
    of a cylinder and then calculates the number of 1" gumballs that will fit 
    inside.
    :param: diameter: float, cylinders diameter in inches
    :param: height: float, cylinders height in inches
    :return: num_gumballs: int, # of gumballs that will fit inside cylinder
    """

    # Initiate variables
    GUMBALL_VOLUME = 0.5236 # gumball with 1" diameter
    PERCENT_SOLID = .65 # percentage of cylinder that will contain solids
                        # to account for space between gumballs
    PI = 3.14159265
    diameter = 0.0
    radius = 0.0
    height = 0.0
    cylinder_volume = 0.0
    num_gumballs = 0

    # Inform users the intent of the program
    print_opening_screen()
    
    # Inputs
    diameter = get_float("Enter cylider diameter (in): ")
    height = get_float("Enter cylider height (in): ")

    # Calculate the radius to use in the volume formula
    radius = calculate_radius(diameter)

    # Calculate the volume of cylinder = πr^2h
    # Multiply cylinder volume by 64% to account for empty space
    # between gumballs
    cylinder_volume = calculate_cyl_volume(radius, height)

    # Calculate the number of gumballs and then truncate the decimal
    # portion - we want the whole number of gumballs
    num_gumballs = calculate_gumballs(cylinder_volume)

    # Outputs
    print_results(num_gumballs)

def print_opening_screen():
    """
    Prints the purpose of the program.
    :param: none
    :return: none
    """
    print("Gumball Estimator!")
    print('Enter the dimensions of a cylinder jar and I will')
    print('tell you how many 1" gumballs it will take to fill!\n')

def get_float(text):
    """
    Converts measurements in text to decimal values
    :param: text:string, input from user
    :return: float, text converted to float
    """
    sentence = ""
    sentence = float(input(text))
    return sentence

def calculate_radius(diameter):
    """
    Calculates the radius by dividng the diameter by 2
    :param: diameter: float, diameter in inches 
    :return: float: radius in inches
    """
    radius = 0.0
    radius = diameter / 2.0
    return radius

def calculate_cyl_volume(radius, height):
    """
    Calculates the volume of the cylinder = πr^2h
    :param: radius: float, radius of cylinder
    :param: height: float, height of cylinder
    :return: cylinder_volume: float, calculated volume of cylinder
    """
    cylinder_volume = 0.0
    PI = 3.14159265
    PERCENT_SOLID = .65 # percentage of cylinder that will contain solids

    cylinder_volume = (PI * (radius ** 2) * height) * PERCENT_SOLID
    return cylinder_volume

def calculate_gumballs(cylinder_volume):
    """
    Calculates the number of gumballs as a whole number
    :param: cylinder_volume: float, calculated volume of the cylinder
    :return: num_gumballs: int, calculated value of gumballs.
    """
    GUMBALL_VOLUME = 0.5236
    num_gumballs = 0
    num_gumballs = int(cylinder_volume / GUMBALL_VOLUME)
    return num_gumballs

def print_results(num_gumballs):
    """
    Prints how many gumballs will fit into cylinder with given dimensions.
    :param: num_gumballs: int, number of gumballs to fit 
    :return: none
    """
    print("\nThe jar will hold {:,} gumballs!".format(num_gumballs))

    print("\nGoodbye!")

if __name__ == "__main__":
    main()