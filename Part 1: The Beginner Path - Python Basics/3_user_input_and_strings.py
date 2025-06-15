# -*- coding: utf-8 -*-
"""
Part 1, Lesson 3: User Input and Strings

Author: dunamismax
Date: 06-15-2025

This file serves as the lesson and demonstration for getting user
input and performing basic string manipulations, including formatting
with f-strings and using string methods.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So far, our programs have run from top to bottom without any interaction.
To create truly useful programs, we need to be able to get data from the user.

In this lesson, you will learn three crucial skills:
1.  How to pause the program and ask the user for input using the `input()` function.
2.  How to format strings beautifully and easily using F-STRINGS.
3.  How to clean up and modify text using built-in STRING METHODS.
'''

# The main execution block starts here.
if __name__ == "__main__":
    
    # --- Part 1: Getting User Input with input() ---

    # The built-in `input()` function is our tool for getting data from the user.
    # When Python runs this line, it will:
    #   1. Display the text inside the parentheses (this is called the PROMPT).
    #   2. Pause the program and wait for the user to type something and press Enter.
    #   3. Take whatever the user typed and return it as a STRING.

    print("--- Part 1: Using the input() function ---")
    
    # We ask for the user's name and store their response in the `user_name` variable.
    user_name = input("Please enter your name: ")
    
    # We then print the value that is now stored in our variable.
    print("The value you entered is:")
    print(user_name)
    
    # CRITICAL POINT: The `input()` function ALWAYS returns a string, even if the
    # user types numbers. We will learn how to convert strings to numbers in a
    # future lesson.
    user_age_string = input("\nPlease enter your age: ")
    print("The type of the age you entered is:")
    print(type(user_age_string)) # This will show <class 'str'>


    # --- Part 2: Formatting with F-Strings ---

    # Now that we have the user's name, let's greet them personally. We could try
    # to "add" strings together using the `+` operator, but it can get messy.
    #
    # A much better, more modern, and more readable way is using an F-STRING.
    #
    # An F-STRING is created by putting the letter `f` before the opening quote
    # of a string. This allows you to embed variables directly inside the string
    # by placing them within curly braces `{}`.

    print("\n--- Part 2: Formatting with F-Strings ---")

    # Create a greeting using an f-string.
    # Python will replace `{user_name}` with the value stored in that variable.
    greeting_message = f"Hello, {user_name}! It's a pleasure to meet you."
    
    print(greeting_message)


    # --- Part 3: Cleaning Input with String Methods ---
    
    # User input can be unpredictable. People might add extra spaces by accident
    # or use inconsistent capitalization.
    #
    # A METHOD is a function that "belongs" to an object (like a string). You call
    # a method using a dot `.` after the variable name.
    
    print("\n--- Part 3: Cleaning up user input ---")
    
    # Let's ask a question where the user might add extra spaces or use caps.
    messy_input = input("\nType a message, maybe with extra spaces at the ends: ")
    print(f"Your original input was: '{messy_input}'")

    # The `.strip()` method removes any whitespace (spaces, tabs, newlines) from
    # the beginning and end of a string.
    stripped_input = messy_input.strip()
    print(f"After .strip():          '{stripped_input}'")
    
    # The `.lower()` method converts the entire string to lowercase.
    # This is great for case-insensitive comparisons.
    lower_input = stripped_input.lower()
    print(f"After .lower():         '{lower_input}'")
    
    # The `.upper()` method converts the string to uppercase.
    upper_input = stripped_input.upper()
    print(f"After .upper():         '{upper_input}'")

    # You can CHAIN methods together. The methods are applied from left to right.
    # This is a very common and powerful pattern in Python.
    print("\n--- Chaining Methods ---")
    favorite_food = input("What's your favorite food? ")
    
    # Here, we get the input, immediately strip whitespace, and then convert to lowercase.
    cleaned_food = favorite_food.strip().lower()

    print(f"Ah, so you like {cleaned_food}. Excellent choice!")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you learned how to make your programs interactive.
1.  The `input()` function pauses the program and captures user input as a STRING.
2.  F-STRINGS (e.g., `f"Hello, {variable}"`) are the best way to format strings
    by embedding variables directly inside them.
3.  METHODS are functions attached to objects. You learned about string methods
    like `.strip()` to remove leading/trailing whitespace and `.lower()`/`.upper()`
    to change the case of a string.
4.  You can CHAIN methods together (e.g., `input().strip().lower()`) to perform
    multiple operations in one clean line.

HOW TO RUN THIS CODE:

1.  Save this file as `3_user_input_and_strings.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 3_user_input_and_strings.py`
'''