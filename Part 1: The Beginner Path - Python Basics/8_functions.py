# -*- coding: utf-8 -*-
"""
Part 1, Lesson 8: Functions

Author: dunamismax
Date: 06-15-2025

This file explains and demonstrates how to define and use functions in
Python. It covers defining functions, passing arguments, returning values,
and the importance of docstrings for documentation.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Lesson 8! As our programs grow, we find ourselves writing the same
pieces of code over and over. This is inefficient and makes our code hard to
read and maintain. The solution is the FUNCTION.

A FUNCTION is a named, reusable block of code that performs a specific task.
You've already been using built-in functions like `print()`, `input()`, and `int()`.
Now, you will learn how to create your own!

Using functions follows a core programming principle: DRY (Don't Repeat Yourself).

Key concepts we will cover:
- DEFINING a function with the `def` keyword.
- CALLING a function to execute its code.
- Passing data to functions using ARGUMENTS (also called PARAMETERS).
- Getting data back from functions using the `return` keyword.
- Documenting functions with DOCSTRINGS.
'''

# --- Part 1: Defining and Calling a Simple Function ---

# We define functions at the top level of our script.
# The `def` keyword starts the function definition, followed by the function's
# name, parentheses `()`, and a colon `:`.
# All the code belonging to the function must be indented.

def say_hello():
    """This is a simple function that prints a fixed greeting."""
    print("Hello! This message is from inside a function.")


# --- Part 2: Functions with Arguments (Parameters) ---

# To make functions more flexible, we can pass data into them.
# The variables listed inside the parentheses of the function definition
# are called PARAMETERS.

def greet_user(name):
    """
    Greets a user personally.
    
    This function takes one argument, `name`, and uses it in the greeting.
    """
    # `name` is a variable that exists only inside this function.
    print(f"Hello, {name}! Welcome to the world of functions.")


# --- Part 3: Functions that Return a Value ---

# Functions can perform a calculation and send a result BACK to the code that
# called it. This is done with the `return` keyword. When `return` is executed,
# the function immediately stops and sends back the specified value.

def add_numbers(num1, num2):
    """
    Takes two numbers as arguments, adds them, and returns the sum.
    """
    sum_result = num1 + num2
    return sum_result # Send this value back to the caller


# --- Part 4: Docstrings and a Complete Example ---

# A DOCSTRING (documentation string) is a multi-line string placed as the
# very first statement in a function's body. It explains what the function
# does, its parameters, and what it returns. It's a critical practice for
# writing clear, professional code.

def calculate_rectangle_area(length, width):
    """Calculates the area of a rectangle.

    Args:
        length (int or float): The length of the rectangle.
        width (int or float): The width of the rectangle.

    Returns:
        int or float: The calculated area of the rectangle.
    """
    if length < 0 or width < 0:
        # It's good practice to handle bad input.
        return 0 # Return 0 for invalid dimensions.
    
    area = length * width
    return area


# =====================================================================
# The main execution block starts here.
# We DEFINE functions outside this block, but we CALL them inside it.
# =====================================================================
if __name__ == "__main__":

    # --- Calling our functions ---

    print("--- Part 1: Calling a simple function ---")
    # To run the code inside a function, you "call" it by its name.
    say_hello()
    say_hello() # We can call it as many times as we want!

    print("\n--- Part 2: Calling a function with an argument ---")
    # When we call the function, the value we provide ("Alice") is the ARGUMENT.
    # This value gets assigned to the `name` parameter inside the function.
    greet_user("Alice")
    greet_user("Bob")

    print("\n--- Part 3: Calling a function that returns a value ---")
    # We call the function and store its return value in a variable.
    total = add_numbers(5, 7)
    print(f"The result of add_numbers(5, 7) is: {total}")
    
    another_total = add_numbers(100, -30)
    print(f"The result of add_numbers(100, -30) is: {another_total}")
    
    # We can also use the function's return value directly.
    print(f"A third result is: {add_numbers(1.5, 2.5)}")

    print("\n--- Part 4: Using our documented function ---")
    rect_area = calculate_rectangle_area(10, 5)
    print(f"The area of a 10x5 rectangle is: {rect_area}")
    
    invalid_area = calculate_rectangle_area(10, -5)
    print(f"The area with an invalid width is: {invalid_area}")


'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you learned the fundamentals of functions, one of the most
important concepts in all of programming.
1.  FUNCTIONS are defined with the `def` keyword and allow you to create
    named, reusable blocks of code. This is the DRY principle in action.
2.  You CALL a function to execute its code.
3.  You can pass data into functions via ARGUMENTS, which are received by the
    function's PARAMETERS.
4.  The `return` keyword allows a function to send a value back to the caller.
5.  DOCSTRINGS (`"""..."""`) are the standard way to document your functions,
    explaining their purpose, arguments, and return values.

HOW TO RUN THIS CODE:

1.  Save this file as `8_functions.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 8_functions.py`
'''