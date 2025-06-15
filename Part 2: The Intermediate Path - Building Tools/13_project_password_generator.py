# -*- coding: utf-8 -*-
"""
Part 2, Lesson 13: Project: Password Generator

Author: dunamismax
Date: 06-15-2025

This file is a project that combines many concepts learned so far,
including functions, loops, user input, conditional logic, exception
handling, and modules, to create a practical, useful tool.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

PROJECT BRIEF: A CUSTOMIZABLE PASSWORD GENERATOR

Welcome to your first major project! The goal is to build a command-line
tool that generates a strong, random password based on user specifications.

This project will be a true test of your skills so far, combining many of
the concepts we've covered into a single, cohesive program:
-   FUNCTIONS (`def`): To organize our code into logical, reusable blocks.
-   USER INPUT (`input()`): To ask the user for their desired password criteria.
-   EXCEPTION HANDLING (`try...except`): To gracefully handle invalid input, like
    a user entering text where a number is expected.
-   CONDITIONAL LOGIC (`if/else`): To determine which character types to include.
-   LOOPS (`for`): To build the password character by character.
-   MODULES (`import`): We will heavily use the `random` module to ensure our
    passwords are unpredictable. We'll also use the `string` module, a handy
    part of the standard library that provides pre-defined strings of
    character sets (like all lowercase letters, all digits, etc.).

Let's build a real tool!
'''

# We need the `random` module for choosing characters and shuffling.
import random
# The `string` module is convenient; it has pre-made strings of characters.
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    """
    Generates a random password based on specified criteria.

    Args:
        length (int): The desired length of the password.
        use_letters (bool): Whether to include letters (a-z, A-Z).
        use_numbers (bool): Whether to include numbers (0-9).
        use_symbols (bool): Whether to include symbols (!@#$, etc.).

    Returns:
        str: The generated password, or None if no character types are selected.
    """
    
    # --- Step 1: Build the pool of possible characters ---
    
    character_pool = ""
    if use_letters:
        # string.ascii_letters is a pre-defined string "abc...xyzABC...XYZ"
        character_pool += string.ascii_letters
    if use_numbers:
        # string.digits is "0123456789"
        character_pool += string.digits
    if use_symbols:
        # string.punctuation contains common symbols like !@#$%^&*()
        character_pool += string.punctuation
        
    # If the user selected no character types, we can't generate a password.
    # We return `None` to signal that generation failed.
    if not character_pool:
        return None
        
    # --- Step 2: Build the password ---
    # We'll build the password as a LIST of characters first, because strings
    # are immutable and lists are mutable, making them easier to shuffle.
    
    password_chars = []
    
    # To guarantee the password meets the criteria, we'll add at least one of
    # each requested character type first.
    if use_letters:
        password_chars.append(random.choice(string.ascii_letters))
    if use_numbers:
        password_chars.append(random.choice(string.digits))
    if use_symbols:
        password_chars.append(random.choice(string.punctuation))
        
    # --- Step 3: Fill the rest of the password length ---
    # We calculate how many more characters we need to add.
    remaining_length = length - len(password_chars)
    
    # Add the remaining characters by picking randomly from the entire pool.
    for _ in range(remaining_length):
        password_chars.append(random.choice(character_pool))
        
    # --- Step 4: Shuffle and Finalize ---
    # Right now, the first characters would always be a letter, then a number,
    # etc. We must SHUFFLE the list to make their positions random.
    random.shuffle(password_chars)
    
    # Join the list of characters back into a single string and return it.
    return "".join(password_chars)


def main():
    """The main function to drive the user interaction."""
    
    print("--- Welcome to the Python Password Generator! ---")
    
    while True: # Loop until we get valid input for the length.
        try:
            length_input = input("Enter the desired password length (e.g., 16): ")
            length = int(length_input)
            
            # A password should have a reasonable length.
            if length < 4:
                print("Password length should be at least 4 for security. Please try again.")
                continue # Skip the rest of this loop and ask again.
            
            break # Exit the loop if int() was successful and length is valid.

        except ValueError:
            print("Invalid input. Please enter a whole number for the length.")
    
    # A helper function to make asking yes/no questions easier.
    def ask_yes_no(prompt):
        while True:
            answer = input(prompt).lower().strip()
            if answer in ["y", "yes"]:
                return True
            elif answer in ["n", "no"]:
                return False
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    # Ask the user for character type preferences.
    include_letters = ask_yes_no("Include letters (a-z, A-Z)? (y/n): ")
    include_numbers = ask_yes_no("Include numbers (0-9)? (y/n): ")
    include_symbols = ask_yes_no("Include symbols (!@#$)? (y/n): ")
    
    # Generate the password by calling our function.
    password = generate_password(length, include_letters, include_numbers, include_symbols)
    
    # Print the final result.
    if password:
        print("\n------------------------------------")
        print(f"Your generated password is: {password}")
        print("------------------------------------")
    else:
        # This happens if the user answered 'no' to all character types.
        print("\nCannot generate a password. You must select at least one character type.")


# This is the entry point of our script.
if __name__ == "__main__":
    # We call our main function to start the program.
    main()

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations on building your first complete, practical tool in Python!

This project reinforced how individual concepts come together to create a
functional application. We defined a core `generate_password` function to
handle the logic and a `main` function to handle the user interaction.

We saw the power of the `random` module for security-related tasks and learned
about the convenient `string` module for accessing common character sets.
Most importantly, we used `try...except` to make our program robust and
prevent it from crashing on bad user input.

This is a milestone in your journey. You're no longer just learning syntax;
you're building software.

HOW TO RUN THIS CODE:

1.  Save this file as `13_project_password_generator.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 13_project_password_generator.py`
5.  Follow the prompts to create your own custom password!
'''