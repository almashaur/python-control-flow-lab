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

