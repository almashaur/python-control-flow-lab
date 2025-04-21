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
