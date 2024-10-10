def main():

    miles = 0.0
    gallons = 0.0
    mpg = 0.0

    print_welcome()

    miles = get_miles()
    gallons = get_gallons()

    mpg = calculate_mpg(miles, gallons)

    print_mpg(mpg)


def get_miles():
    """ 
    Asks user for the number of gallons used.
    :param: none
    :return: none
    """ 
    miles = 0.0
    miles = float(input("Enter the number of miles driven: "))
    return miles

def get_gallons():
    """
    Asks user for the number of gallons used.
    :param: none
    :return: none
    """
    gallons = 0.0
    gallons = float(input("Enter the number of gallons of gas used: "))
    return gallons

def calculate_mpg(miles, gallons):
    """
    Calculates the miles per gallon based on miles driven and gallons used.
    :param: miles: float, number of miles driven
    :param: gallons: float, number of gallons used
    :return: float, calculated miles per gallon
    """
    mpg = 0.0
    mpg = miles / gallons
    return mpg

def print_welcome():
    """
    Prints welcoming message to inform the purpose of program
    :param: none
    :return: none
    """
    print("Welcome to the MPG Calculator!\n")

def print_mpg(mpg):
    """
    Prints the miles per gallon, formatted to 1 decimal place
    :param: mpg: float, miles per gallon
    :return: none
    """
    print("\nYour car gets", format(mpg, ".1f"), "miles per gallon!")


if __name__ == "__main__":
    main()