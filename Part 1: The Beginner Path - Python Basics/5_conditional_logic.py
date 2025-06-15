# -*- coding: utf-8 -*-
"""
Part 1, Lesson 5: Conditional Logic

Author: dunamismax
Date: 06-15-2025

This file explains and demonstrates conditional logic using if, elif,
and else statements. It shows how to control the flow of a program
based on different conditions and highlights the importance of indentation.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Lesson 5! This is where programming starts to get really powerful.
So far, our scripts have run every single line of code from top to bottom.
But what if we only want to run certain code if a specific condition is met?

This is called CONDITIONAL LOGIC, and it's how we make programs "think" and
make decisions. The comparison and logical operators you learned in the last
lesson are the heart of this process.

The keywords we will learn are:
- `if`:      Executes a block of code if its condition is true.
- `elif`:    (short for "else if") Executes if the previous condition was false,
             but this new condition is true.
- `else`:    Executes if none of the preceding conditions were true.

A CRITICAL CONCEPT: INDENTATION
In many languages, code blocks are defined by curly braces `{}`. In Python,
code blocks are defined by their INDENTATION (the spaces at the beginning of
a line). This is not just for style; it is part of Python's SYNTAX. You will
see this in action below. The standard is to use 4 spaces for each level
of indentation.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: The `if` Statement ---
    # The `if` statement runs a block of code only when its condition is True.
    # The syntax is `if condition:`, where the condition is an expression that
    # evaluates to a boolean (True or False).

    print("--- Part 1: The `if` statement ---")
    user_age_str = input("Please enter your age: ")

    # IMPORTANT: TYPE CASTING
    # The `input()` function always gives us a string. We cannot compare a string
    # "21" with a number 18. We must first convert the string to an integer.
    # This process is called TYPE CASTING. We use `int()` to convert to an integer.
    age = int(user_age_str)

    if age >= 18:
        # This line is INDENTED, so it is part of the `if` block.
        # It will only run if the condition `age >= 18` is True.
        print("Congratulations! You are old enough to vote.")

    print("This line runs no matter what, because it is not indented.")

    # --- Part 2: The `if-else` Statement ---
    # The `else` statement provides a block of code to run if the `if` condition
    # is False. It acts as a "catch-all" for when the `if` is not met.

    print("\n--- Part 2: The `if-else` statement ---")
    temperature_str = input("What is the temperature in Celsius? ")
    temperature = int(temperature_str)

    if temperature > 25:
        print("It's hot! You should wear shorts.")
    else:
        # This block runs only if `temperature > 25` is False.
        print("It's not that hot. Maybe wear trousers.")


    # --- Part 3: The `if-elif-else` Chain ---
    # What if you have more than two possibilities? You can use `elif` to check
    # multiple conditions in a sequence. Python will check each condition from
    # top to bottom and run the code for the FIRST one that is True.
    # If none are True, the `else` block runs.

    print("\n--- Part 3: The `if-elif-else` chain ---")
    score_str = input("Enter your test score (0-100): ")
    score = int(score_str)

    if score >= 90:
        grade = "A"
    elif score >= 80:
        # This only gets checked if `score >= 90` was False.
        grade = "B"
    elif score >= 70:
        # This only gets checked if the two above were False.
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        # This runs if none of the above conditions were met.
        grade = "F"
    
    print(f"With a score of {score}, your grade is {grade}.")


    # --- Part 4: Combining with Logical Operators ---
    # You can create complex conditions using the `and`, `or`, and `not`
    # operators you learned about in the previous lesson.

    print("\n--- Part 4: Using logical operators ---")
    
    # We can reuse the `age` and `temperature` variables from earlier.
    # Let's check if the user is a child (under 13) AND if it's cold (under 10 C).
    
    if age < 13 and temperature < 10:
        print("You're a child and it's cold. Make sure to wear a warm jacket!")
    elif age >= 65 and temperature < 10:
        print("As a senior, please be sure to dress warmly when it's this cold.")
    else:
        print("Enjoy the weather!")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this crucial lesson, you learned how to control your program's flow:
1.  CONDITIONAL LOGIC lets your program make decisions.
2.  The `if` statement runs code only if a condition is `True`.
3.  The `else` statement provides an alternative block to run if the `if`
    condition is `False`.
4.  The `elif` statement allows you to check multiple alternative conditions in order.
5.  INDENTATION (using 4 spaces) is how Python defines code blocks. It is not
    optional; it is a fundamental part of the language's syntax.
6.  TYPE CASTING, like using `int()`, is necessary to convert data from one
    type to another (e.g., from a string provided by `input()` to a number).

HOW TO RUN THIS CODE:

1.  Save this file as `5_conditional_logic.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 5_conditional_logic.py`
'''