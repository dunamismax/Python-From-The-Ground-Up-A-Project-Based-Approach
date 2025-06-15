# -*- coding: utf-8 -*-
"""
Part 1, Lesson 1: Hello, World!

Author: dunamismax
Date: 06-15-2025

This file is your very first Python program and lesson.
The lesson is taught through the comments in this file. Read them
from top to bottom to understand what's happening.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to your first lesson in "Python From The Ground Up"! The journey to
mastering Python is fun, empowering, and it all begins right here.

In this lesson, you will learn how to run a Python file and display a message
on the screen. This simple act is a rite of passage for every programmer.

WHAT IS A PYTHON INTERPRETER?
Some programming languages, like C or C++, use a COMPILER. A compiler reads
your entire program and translates it into a separate machine-code file (like an
.exe file on Windows) that the computer can run directly.

Python, on the other hand, uses an INTERPRETER. The Python interpreter reads
your code file (`.py` file) line by line and executes each command directly.
There is no separate compilation step. This makes the development process faster
and more interactive, which is one of the reasons Python is so popular.
'''

# --- The Main Execution Block ---

# In Python, it is a very strong convention to put your main script logic
# inside a special block that starts with `if __name__ == "__main__":`.
#
# We will explain exactly what this line means in a later lesson. For now,
# just know that this is the official starting point of our program. All the
# code indented underneath it is what will run when you execute this file.
if __name__ == "__main__":
    
    # This is the line that does the work!
    # `print()` is a built-in FUNCTION that Python provides for us. A function
    # is a named block of code that performs a specific task. In this case,
    # the `print()` function's task is to display output on the screen.
    #
    # The value we put inside the parentheses is called an ARGUMENT. Here, we are
    # giving the `print` function one argument.
    #
    # The text itself, "Hello, World!", enclosed in double quotes, is called
    # a STRING. A string is a sequence of characters, used to represent text.
    print("Hello, World!")
    
    # You might notice that, unlike some other languages, we do not need a
    # special character like a semicolon (;) at the end of the line. Python
    # uses newlines to separate statements.
    #
    # Also, the program simply ends when it runs out of lines to execute inside
    # this block. There's no need for a `return 0` or `exit` statement for
    # a simple script like this.

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

HOW TO RUN THIS CODE:

1.  Save this file as `1_hello_world.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Use the Python interpreter to run the file by typing the following command
    and pressing Enter:

    `python 1_hello_world.py` 
    
    (Note: On some systems, especially macOS or Linux, you might need to use
    `python3` instead of `python`):
    `python3 1_hello_world.py`

You should see the text "Hello, World!" printed to your console.
Congratulations on running your first Python program!
'''