# -*- coding: utf-8 -*-
"""
Part 1, Lesson 2: Variables and Data Types

Author: dunamismax
Date: 06-15-2025

This file serves as the lesson and demonstration for variables and
the core data types in Python. It explains the concepts through
structured comments and provides a runnable example.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to your second lesson! In the first lesson, we printed a fixed message,
"Hello, World!". But programs are most useful when they can work with information
that can change. To do that, we need to store data.

In programming, we store data in VARIABLES.

A VARIABLE is a named storage location in the computer's memory. Think of it
like a labeled box where you can keep a piece of information. You give the box a
name (the variable name), and you can put data inside it, look at what's inside,
or replace it with new data.
'''

# --- Part 1: Declaring and Using Variables ---

# To create a variable in Python, you use the assignment operator, which is the
# equals sign (=).
#
# The syntax is: variable_name = value
#
# Below, we create a variable named `greeting` and assign it the string value
# "Hello, Python Student!".

# A note on naming variables:
# - Names must start with a letter or an underscore (_).
# - They cannot start with a number.
# - They can only contain alpha-numeric characters (a-z, A-Z, 0-9) and underscores.
# - Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables).
# - The Python community convention is to use `snake_case` for variable names
#   (all lowercase letters with words separated by underscores).

# --- Part 2: Python's Core Data Types ---

# The data we store in variables has a TYPE. A data type tells Python what kind
# of data a variable holds, which affects what you can do with it. For example,
# you can do math with numbers, but not with text.
#
# Python is a DYNAMICALLY TYPED language. This means you don't have to tell
# Python what the data type is beforehand. Python automatically figures it out
# when you assign a value to the variable.

# The main execution block starts here.
if __name__ == "__main__":
    
    # We declare a variable `greeting` and assign a string to it.
    greeting = "Hello, Python Student!"
    
    # Now, we can use the variable's name in our print function.
    # This will print the *value* that the variable is holding.
    print(greeting)

    print("\n--- Let's explore the core data types! ---\n")

    # 1. STRING (str): Used for text. Enclosed in single ('') or double ("") quotes.
    student_name = "Alice"
    print("The variable 'student_name' holds the value:")
    print(student_name)

    # 2. INTEGER (int): Used for whole numbers (no decimal point).
    student_age = 21
    print("\nThe variable 'student_age' holds the value:")
    print(student_age)

    # 3. FLOAT (float): Used for numbers with a decimal point.
    student_gpa = 3.85
    print("\nThe variable 'student_gpa' holds the value:")
    print(student_gpa)

    # 4. BOOLEAN (bool): Used to represent truth values. Can only be `True` or `False`.
    #    Note that `True` and `False` are capitalized.
    is_enrolled = True
    print("\nThe variable 'is_enrolled' holds the value:")
    print(is_enrolled)

    # --- Part 3: Checking a Variable's Type and Dynamic Typing in Action ---

    # Python has a built-in function called `type()` that lets us inspect the
    # data type of a variable. This is very useful for understanding your code.
    
    print("\n--- Using the type() function ---\n")
    print("The type of 'student_name' is:")
    print(type(student_name))
    
    print("\nThe type of 'student_age' is:")
    print(type(student_age))
    
    print("\nThe type of 'student_gpa' is:")
    print(type(student_gpa))
    
    print("\nThe type of 'is_enrolled' is:")
    print(type(is_enrolled))
    
    # Because Python is DYNAMICALLY TYPED, you can reassign a variable to a
    # completely different type of data.
    print("\n--- Dynamic Typing Example ---")
    some_variable = 100
    print("The variable 'some_variable' starts as an integer. Value:", some_variable)
    print("Type:", type(some_variable))
    
    # Now let's reassign it to a string.
    some_variable = "Now I am a string."
    print("\nIt has been reassigned. Its new value is:", some_variable)
    print("Type:", type(some_variable))
    # While you *can* do this, it's generally good practice to keep a variable's
    # type consistent to avoid confusion.

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you learned:
1.  A VARIABLE is a name for a location in memory used to store data.
2.  You create variables with the assignment operator `=`.
3.  The core data types are STRINGS (`str`), INTEGERS (`int`), FLOATS (`float`),
    and BOOLEANS (`bool`).
4.  Python is DYNAMICALLY TYPED, meaning it automatically detects a variable's type,
    and the type can change if you reassign the variable.
5.  The `type()` function can be used to see what type of data a variable holds.

HOW TO RUN THIS CODE:

1.  Save this file as `2_variables_and_types.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 2_variables_and_types.py`
'''