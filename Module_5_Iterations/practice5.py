#******************************************************************************
# Author:           Joshua Garza
# Lab:              Practice #5
# Date:             10/22/2024
# Description:      program that propmpts user for a series of integers and 
#                   returns the sum, average, min and max values of series.  
# Input:            number: int
# Output:           Sum, average, min and max values of series
# Sources:          Practice 5 specifications.
#                   -Have a main() function.
#                   -Add a while loop to your main() function to execute your 
#                       program until the user wants to quit.
#                   -Have a function for every input, process (calculation), 
#                       and output (IPO). 
#                   -Declare result variables in functions. Do not return an 
#                       equation. Assign the result variable(s) the equation 
#                       result, the return the result variable(s).
#                   -Include a function comment in each function with a 
#                       description, parameters, and return values. 
#                   -Input a series of values, one value each time through the
#                       loop.
#                   -Within the loop, find ways to calculate if the newly 
#                       entered integer is new minimum or new maximum number
#                       as well as how to add it to a running total and count
#                       how many integers have been entered so far (the last 
#                       two are critical for ).
#                   -Print out the sum of all the integers, the number of 
#                       integers entered, the average amount of all those 
#                       integers            
#******************************************************************************

#******************************************************************************
# Sample Run:
# 
#                           Welcome! 
# 
# This program will output the sum, average, min and max values based 
#                   on the values you provide. 
# 
#                   Would you like to try? Yes
#
#                 Enter values (0  when finished): 13 
#                 Enter values (0  when finished): 27
#                 Enter values (0  when finished): 48
#                 Enter values (0  when finished): 0
# 
# You've entered 3 values to calculate. Here are the stats:
# 
# Sum: 88
# Average: 29.33
# Min: 13
# Max: 48
# 
#                  Would you like to try again? No
# 
# 
# Thanks for playing, see you next time!
#******************************************************************************

def main():
    """ Program that prompts user to enter an undefined amount of numbers and 
    provides the statistical data associated. (Sum, Min, Max, Average)
    :param: none
    :return: none
    """

    playAgain = True

    # Welcome users and inform purpose of program
    printGreeting()

    # Ask user if they want to play
    playAgain = playRequest("Do you want to play? (Y)es or (N)o :")

    # Ask for Values as long as boolean is true. 
    while playAgain == True:
        getValues()

        playAgain = playRequest("Do you want to play again? (Y)es or (N)o :")


def printGreeting():
    """ 
    Prints a greeting to the screen and details the purpose of program.
    :param: none
    :return: none
    """
    print("\n\t\tWelcome,\n")
    print("""This program will output the sum, average, min and max values
        based on the values you provide.\n""")

def playRequest(message):
    """
    Prompts the user to answer a yes or No question.
    :param: message: str, the question to ask.
    :return: again: bool, True if Yes, False if No
    """
    answer = ""
    again = False

    answer = input(message).lower()

    if answer != "y":
        printGoodbye()
    else:
        again = True

    return again

def getValues():
    """ 
    Prompts the user to enter a series of integers, calculates the sum, 
    average, minimum, and maximum of the entered values, and passes these 
    to a results display function.

    The user inputs integers one by one, and the input terminates when the 
    user enters 0. If no values are entered, it informs the user that no 
    numbers were entered.

    :param: none
    :return: none
    """
    total = 0
    count = 0
    min_val = 0
    max_val = 0

    while True:
        number = int(input("Enter a number (0 to finish): "))

        if number == 0:
            break
        else:
            total += number
            count += 1

        if min_val is 0 or number < min_val:
            min_val = number
        if max_val is 0 or number > max_val:
            max_val = number

    if count > 0:
        printResults(total, count, min_val, max_val)
    else:
        print("No numbers were entered.")

def printResults(total, count, min_val, max_val):
    """ 
    Prints the sum, average, minimum, and maximum of the numbers entered.
    :param total: int, the sum of all numbers entered
    :param count: int, the count of numbers entered
    :param min_val: int, the smallest number entered
    :param max_val: int, the largest number entered
    :return: none
    """
    average = 0
    average = total / count
    print(f"\nYou've entered {count} values to calculate. Here are the stats:\n")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")

def printGoodbye():
    """
    Informs the user the program is finished and will be closing.
    :param: none
    :return: none
    """ 
    print("\nThanks for playing, see you next time!")

if __name__ == "__main__":
    main()