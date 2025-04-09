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

    # Prompt the user for input
    letter = input("Please enter a letter (a-z or A-Z): ").strip()

    # Check if the input is a single alphabetical character
    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter.")
        return

    # Convert to lowercase for easier comparison
    letter_lower = letter.lower()

    # Determine if the letter is a vowel or consonant
    if letter_lower in 'aeiou':
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")
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
    # Define the minimum voting age
    voting_age = 18

    # Prompt the user for their age
    try:
        age = int(input("Please enter your age: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Check if the age is a negative number
    if age < 0:
        print("Invalid input. Age cannot be negative.")
        return

    # Determine if the user is eligible to vote
    if age >= voting_age:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

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
    # Prompt the user for the dog's age
    try:
        dog_age = int(input("Input a dog's age: ").strip())
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Check if the age is negative
    if dog_age < 0:
        print("Invalid input. Age cannot be negative.")
        return

    # Calculate the dog's age in dog years
    if dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = 20 + (dog_age - 2) * 7

    # Print the result
    print(f"The dog's age in dog years is {dog_years}.")

# Call the function
calculate_dog_years()


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
    # Input month and day
    month = input("Enter the month of the year (Jan - Dec): ").strip().capitalize()
    day = input("Enter the day of the month: ").strip()
    try:
        day = int(day)
    except ValueError:
        print("Invalid input. Please enter a valid day.")
        return
    # Validate month and day
    if month not in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        print("Invalid month. Please enter a valid month (Jan - Dec).")
        return
    
    # Make sure the day is valid for the month
    if month in ['Apr', 'Jun', 'Sep', 'Nov'] and day > 30:
        print("Invalid day. This month has only 30 days.")
        return
    elif month == 'Feb' and day > 29:
        print("Invalid day. February has only 29 days.")
        return
    elif month == 'Feb' and day == 29 and not (day % 4 == 0 and (day % 100 != 0 or day % 400 == 0)):
        print("Invalid day. February has only 28 days in non-leap years.")
        return
    elif day > 31:
        print("Invalid day. This month has only 31 days.")
        return
    
    # Determine the season
    if (month == 'Dec' and day >= 21) or (month == 'Jan') or (month == 'Feb') or (month == 'Mar' and day < 20):
        season = "Winter"
    elif (month == 'Mar' and day >= 20) or (month == 'Apr') or (month == 'May') or (month == 'Jun' and day < 21):
        season = "Spring"
    elif (month == 'Jun' and day >= 21) or (month == 'Jul') or (month == 'Aug') or (month == 'Sep' and day < 22):
        season = "Summer"
    else:
        season = "Fall"

    # Print the result
    print(f"{month} {day:02d} is in {season}.")

    # Call the function
determine_season()
