# ## sIMPLE PYTHON DATA ##
# num_cookies = 0
# num_servings = 0
# total_calories = 0

# COOKIES_PER_SERVING = 3
# CALORIES_PER_COOKIE = 51

# print("Welcome to the Cookie Calorie Calculator!\n")

# num_cookies = int(input("Enter number of cookies eaten: "))

# num_servings = num_cookies / COOKIES_PER_SERVING
# total_calories = num_cookies * CALORIES_PER_COOKIE

# print("\nYou consumed", format(num_servings, ".2f"), "servings!")
# print("That is a total of", total_calories, "calories.")

# print("\nGoodbye!")

## MODULUS ##

def main():
    cents = 1542 # change this to test different amounts
    quarters = 0
    dimes = 0
    nickels = 0
    dollars = 0

    quarters = cents // 25 # number of quarters
    cents = cents % 25     # cents remaining

    # add code to calculate dimes, nickels, cents
    dimes = cents // 10  # number of dimes
    cents = cents % 10  # cents remaining

    nickels = cents // 5
    cents = cents % 5
    

    # print the results
    print('Quarters:', quarters)
    print("Dimes: ", dimes)
    print("Nickels: ", nickels)

main()