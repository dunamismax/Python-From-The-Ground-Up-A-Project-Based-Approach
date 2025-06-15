# -*- coding: utf-8 -*-
"""
Part 2, Lesson 12: Exception Handling

Author: dunamismax
Date: 06-15-2025

This lesson introduces exception handling in Python. It explains what
exceptions are and demonstrates how to use the try...except block to
build robust programs that can handle errors gracefully without crashing.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So far, our programs have been "optimistic." We assume the user will always
enter a valid number, or that the file we want to read will always exist.
But in the real world, things go wrong.

When an unexpected error occurs while your program is running, Python raises an
EXCEPTION. If this exception is not "handled," your program will immediately
CRASH and stop executing. This is a bad experience for the user.

Common examples of exceptions you may have already caused by accident:
- `ValueError`: Trying to convert "hello" to an integer with `int("hello")`.
- `ZeroDivisionError`: Dividing a number by zero.
- `IndexError`: Trying to access `my_list[10]` when the list only has 3 items.
- `KeyError`: Trying to access a dictionary key that doesn't exist.

EXCEPTION HANDLING is the process of anticipating and managing these runtime
errors. Python gives us a powerful structure for this: the TRY...EXCEPT block.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: The Problem - A Crashing Program ---
    # Let's write a simple program that asks for a user's age.
    # If the user types "twenty" instead of "20", the `int()` function will
    # fail and raise a `ValueError`, crashing the script.
    
    print("--- Part 1: A Program That Can Crash ---")
    # age_input = input("Please enter your age: ")
    # age = int(age_input) # This line will crash if input is not a number.
    # print(f"Next year, you will be {age + 1}.")
    # print("This line will never be reached if the program crashes.\n")
    #
    # We've "commented out" the code above so this script can run fully.
    # You can uncomment it to see the crash for yourself.
    print("The code for this section is commented out to prevent a crash.")


    # --- Part 2: The Solution - The `try...except` Block ---
    # To prevent a crash, we wrap the "risky" code in a `try` block.
    # If an error occurs inside `try`, Python immediately jumps to the `except`
    # block and runs that code instead of crashing.
    
    print("\n--- Part 2: The `try...except` Block ---")

    try:
        # This is the "risky" code that might cause an exception.
        age_input = input("Please enter your age (I won't crash this time): ")
        age = int(age_input)
        print(f"Next year, you will be {age + 1}.")
    except:
        # This code only runs if an error occurred in the `try` block.
        print("Oops! That wasn't a valid number. Please enter a numerical age.")

    print("Program execution continues after the `try...except` block.")


    # --- Part 3: Handling Specific Exceptions ---
    # A plain `except:` block catches *any* and *all* exceptions. This is
    # generally bad practice because it can hide bugs you weren't expecting.
    # It's much better to catch only the specific exceptions you know how to
    # handle.
    
    print("\n--- Part 3: A Robust Division Calculator ---")
    
    # This calculator can have two specific problems:
    # 1. User enters text instead of a number (`ValueError`).
    # 2. User tries to divide by zero (`ZeroDivisionError`).
    
    try:
        numerator_str = input("Enter the numerator: ")
        numerator = int(numerator_str)
        
        denominator_str = input("Enter the denominator: ")
        denominator = int(denominator_str)
        
        result = numerator / denominator
        print(f"The result is: {result}")

    except ValueError:
        # This block ONLY runs if a `ValueError` occurs (e.g., int("abc")).
        print("Error: You must enter valid integers for both numbers.")

    except ZeroDivisionError:
        # This block ONLY runs if a `ZeroDivisionError` occurs.
        print("Error: You cannot divide by zero.")

    print("Calculation attempt finished.")


    # --- Part 4: The `else` and `finally` Clauses ---
    # The `try` statement has two more optional clauses:
    #
    # - `else`: The code in the `else` block runs ONLY IF the `try` block
    #   completed successfully (i.e., no exceptions were raised).
    # - `finally`: The code in the `finally` block runs NO MATTER WHAT. It runs
    #   if the `try` block succeeded, or if an exception was caught. It's
    #   perfect for cleanup code (like closing a file).

    print("\n--- Part 4: `try...except...else...finally` ---")

    try:
        num_input = input("Enter a number to find its reciprocal: ")
        num = float(num_input) # Using float to allow for decimals.
        reciprocal = 1 / num
    
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
    
    except ZeroDivisionError:
        print("Error: Cannot calculate the reciprocal of zero.")
        
    else:
        # This runs only on success! It's good practice to put your
        # "success" logic here.
        print(f"Success! The reciprocal of {num} is {reciprocal}.")
        
    finally:
        # This runs every single time, whether there was an error or not.
        print("This `finally` block always executes.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Exception handling is a fundamental part of writing professional, reliable code.
Instead of letting your program crash, you can anticipate and manage errors.

1.  An EXCEPTION is an error that happens during program execution.
2.  The `try...except` block is the primary tool for handling exceptions.
3.  Risky code goes in the `try` block. Error-handling code goes in the
    `except` block.
4.  It is best practice to catch SPECIFIC exceptions (e.g., `except ValueError:`)
    rather than using a generic `except:`.
5.  The optional `else` block runs only when the `try` block completes
    successfully (no exceptions).
6.  The optional `finally` block runs every time, regardless of whether an
    exception occurred, making it ideal for cleanup actions.

You can now write programs that are much more robust and user-friendly!

HOW TO RUN THIS CODE:

1.  Save this file as `12_exception_handling.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 12_exception_handling.py`
5.  Try entering different inputs (text, numbers, zero) to see how the
    different `except`, `else`, and `finally` blocks are executed.
'''