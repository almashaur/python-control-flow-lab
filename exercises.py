# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    x = input("Enter a letter(a-z or A-Z):").strip().lower()

    # to make sure you submitted a letter
    if x == "":
        print("Enter a letter please")
        return
    
    # to check if the input is a sigle letter
    if x.isalpha() and len(x) == 1:

        # here, we check if the letter is a vowel or consonant
        if x in ['a', 'e', 'i', 'o', 'u']:
            print(f"The letter {x} is a vowel.")
        else:
            print(f"The letter {x} is a consonant.")
    else:
        # as a safety net, a final response for invalid input
        print("Please enter a single valid letter (a-z or A-Z).")
        return
    
# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    #as a preset, the voting age is 18

    age = input("What's your age?  ").strip()
    if age.isnumeric() == False:
        print("You have to enter a number!")
        return
    else:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You are too young to vote. You have to be 18.")

# Call the function
check_voting_eligibility()

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = input("What is your dog's age?: ").strip()

    # prevents errors and checks if its a number before int()
    if dog_age.isnumeric() == False:
        print("You have to enter a number!")
        return
    else:
        dog_age = int(*dog_age)
        if dog_age < 0:
            print("age cant be less than 0!") # cant have a negative age
            return
        elif dog_age <= 2: # first two years
            dog_years = dog_age * 10
        else: # after the first two years
            dog_years = 20 + (dog_age - 2) * 7 #the twenty is the first two years. that is why the dog age also looses two years beause 20 is 2 years
        print(f"The dog's age in dog years is {dog_years}.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    temp = input("Is it cold? (yes/no): ").strip().lower()
    rain = input("Is it raining? (yes/no): ").strip().lower()
    print(temp, rain)

    if temp != "yes" and temp != "no" and rain != "yes" and rain != "no": # makes sure you only inputted yes or no in both
        print("answer the questions with a yes or no please")
        return
    else:
        if temp == "yes" and rain == "yes":
            print("Wear a waterproof coat.") # its both
        elif temp == "yes" and rain == "no":
            print("Wear a warm coat.") # its just cold
        elif temp == "no" and rain == "yes":
            print("Carry an umbrella.") # its just raining 
        else:
            print("Wear light clothing.") # its not cold and not raining

# Call the function
weather_advice()

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.

def determine_season():
    month = input("Enter a month (Jan, Feb, Mar, Apr May, Jun, Jul, Aug, Sep, Oct, Nov, Dec):").strip().lower()

    day = input("Enter the day of the month (a number)").strip()

    valid_months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] # months allowed

    # list of maximum day values based on the month
    max_days = {
        'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 'may': 31,
        'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 'oct': 31,
        'nov': 30, 'dec': 31
    }

    if month not in valid_months:
        print("Month is invalid, please select from the list.") # invalid month
        return
    
    # if the day isnt numeric, it will return an error and leave the function
    if not day.isnumeric():
        print("Day is invalid, please enter a number.") # non numeric day
        return 
    else :
        day = int(day) # since it is numeric, we convert it to an int

    if day < 1 or day > max_days[month]:
        print(f"Day is not in month, please enter a number between 1 and {max_days[month]}.") # day out of bounds
        return
    if month == 'dec' and day >= 21 or month == 'jan' or month == 'feb' or month == 'mar' and day <= 19:
        print (f"{month.capitalize()} {day} is in Winter.")
    elif month == 'mar' and day >= 20 or month == 'apr' or month == 'may' or month == 'jun' and day <= 20:
        print (f"{month.capitalize()} {day} is in Spring.")
    elif month == 'jun' and day >= 21 or month == 'jul' or month == 'aug' or month == 'sep' and day <= 21:
        print (f"{month.capitalize()} {day} is in Summer.") 
    elif month == 'sep' and day >= 22 or month == 'oct' or month == 'nov' or month == 'dec' and day <= 20:
        print (f"{month.capitalize()} {day} is in Fall.")


# Call the function
determine_season()
