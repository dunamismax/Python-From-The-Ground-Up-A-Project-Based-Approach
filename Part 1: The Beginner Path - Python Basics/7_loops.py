# -*- coding: utf-8 -*-
"""
Part 1, Lesson 7: Loops

Author: dunamismax
Date: 06-15-2025

This file explains and demonstrates loops in Python. It covers the
`for` loop for iterating over sequences and the `while` loop for
repeating code based on a condition.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Lesson 7! Imagine you have a list of 100 chores. Would you write
100 `print()` statements? Of course not! Programming provides a powerful way
to perform repetitive tasks without repetitive code. This is done using LOOPS.

A LOOP is a control structure that allows you to execute a block of code
multiple times.

Python has two main types of loops:
1.  The `for` loop: Used for ITERATING over a sequence (like a list, a string,
    or a range of numbers). You use it when you know how many times you want
    the loop to run.
2.  The `while` loop: Repeats a block of code AS LONG AS a certain condition
    is true. You use it when you don't know in advance how many times the loop
    needs to run.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: The `for` Loop ---
    # The `for` loop is perfect for going through each item in a list, one by one.

    print("--- Part 1: The `for` loop with a list ---")
    
    planets = ["Mercury", "Venus", "Earth", "Mars"]
    
    # The syntax is `for <variable> in <sequence>:`
    # For each pass through the loop, the variable `planet` will hold the
    # current item from the `planets` list.
    print("Here are the inner planets:")
    for planet in planets:
        # The indented code block below will run for each item in the list.
        print(f"- {planet}")


    # --- Part 2: The `for` loop with `range()` ---
    # Sometimes, you just want to run a block of code a specific number of times.
    # The `range()` function is perfect for this. It generates a sequence of numbers.

    print("\n--- Part 2: The `for` loop with range() ---")
    
    # `range(5)` generates numbers from 0 up to (but not including) 5.
    # So, it will generate 0, 1, 2, 3, 4.
    print("Counting from 0 to 4:")
    for number in range(5):
        print(f"Current number is: {number}")


    # --- Part 3: The `while` Loop ---
    # A `while` loop continues to run as long as its condition is `True`.
    # This is very powerful, but also dangerous if you're not careful!

    print("\n--- Part 3: The `while` loop ---")
    
    count = 1
    
    # This loop will continue as long as the `count` variable is less than or equal to 5.
    while count <= 5:
        print(f"While loop is at count: {count}")
        
        # CRITICAL STEP: We must change the variable inside the loop so that the
        # condition will eventually become `False`. If we forget this line,
        # `count` will always be 1, `count <= 5` will always be true, and we
        # will have an INFINITE LOOP! You would have to stop the program manually.
        count = count + 1 # Increment the count by 1 for the next pass.
    
    print("The while loop has finished.")


    # --- Part 4: A Practical `while` Loop Example ---
    # `while` loops are great for situations where you're waiting for user input.
    
    print("\n--- Part 4: A practical `while` loop ---")
    
    # We will keep asking for a password until the user gets it right.
    correct_password = "python"
    user_guess = "" # Initialize with an empty string

    while user_guess != correct_password:
        user_guess = input("Enter the password: ").lower().strip()
        
        if user_guess != correct_password:
            print("Incorrect password. Please try again.")

    # This line will only be reached after the loop condition becomes false,
    # which happens when user_guess IS equal to correct_password.
    print("Access granted! Welcome.")


    # --- Part 5: Loop Control with `break` and `continue` ---
    # Sometimes you need to change a loop's behavior mid-execution.
    
    print("\n--- Part 5: `break` and `continue` ---")
    
    # `continue` skips the rest of the current iteration and goes to the next one.
    print("Using 'continue' to skip printing the number 3:")
    for i in range(5): # numbers 0, 1, 2, 3, 4
        if i == 3:
            continue # Skip the print statement for this iteration
        print(f"Number is {i}")
        
    # `break` exits the loop entirely.
    print("\nUsing 'break' to stop the loop when we find the number 3:")
    for i in range(10): # numbers 0 through 9
        print(f"Checking number {i}...")
        if i == 3:
            print("Found it! Breaking the loop.")
            break # Exit the loop immediately
    
    print("Loop finished (or was broken).")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you mastered the concept of loops for task repetition.
1.  LOOPS let you run a block of code multiple times.
2.  The `for` loop is used to ITERATE over a known sequence (like a list) or a
    `range()` of numbers.
3.  The `while` loop runs as long as a condition remains `True`. It's crucial
    to ensure the condition eventually becomes `False` to avoid an INFINITE LOOP.
4.  You learned two loop control statements:
    - `continue`: Skips the current iteration and proceeds to the next.
    - `break`: Exits the loop immediately, regardless of the loop's condition.

HOW TO RUN THIS CODE:

1.  Save this file as `7_loops.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 7_loops.py`
'''