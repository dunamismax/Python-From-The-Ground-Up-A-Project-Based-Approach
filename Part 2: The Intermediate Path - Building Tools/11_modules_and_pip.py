# -*- coding: utf-8 -*-
"""
Part 2, Lesson 11: Modules and pip

Author: dunamismax
Date: 06-15-2025

This file is a lesson on Python modules. It covers importing and using
modules from the standard library (like 'random' and 'datetime') and
introduces 'pip', the tool used to install third-party packages.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

In the last lesson, we used `import os` to get access to functions that
interact with the operating system. The `os` module is just one of hundreds
that come included with Python. This collection of included modules is called
the PYTHON STANDARD LIBRARY.

WHAT IS A MODULE?
A MODULE is simply a Python file (`.py`) containing reusable code. Instead of
writing everything in one giant file, programmers organize related functions,
classes, and variables into modules. This makes code easier to manage, share,
and reuse.

Think of modules as toolkits. If you need tools for math, you import the
`math` module. If you need tools for generating random numbers, you import
the `random` module.

In this lesson, we will explore:
1.  How to `import` modules and use their contents.
2.  Two useful modules from the Standard Library: `random` and `datetime`.
3.  What to do when the tool you need isn't in the Standard Library, which
    introduces `pip` and the Python Package Index (PyPI).
'''

# --- Part 1: Importing and Using a Module (`random`) ---
# The `import` statement makes a module's code available to your script.
# The `random` module contains functions for generating random numbers.

import random

# It's good practice to put all your imports at the top of the file.
# The `datetime` module provides classes for working with dates and times.
import datetime


# The main execution block starts here.
if __name__ == "__main__":

    print("--- Part 1: The `random` module ---")

    # To use a function from an imported module, you use the syntax:
    # `module_name.function_name()`

    # `random.randint(a, b)` returns a random integer between a and b (inclusive).
    random_number = random.randint(1, 10)
    print(f"A random number between 1 and 10 is: {random_number}")

    # `random.choice(sequence)` returns a random element from a sequence (like a list).
    fruits = ["apple", "banana", "cherry", "dragonfruit"]
    random_fruit = random.choice(fruits)
    print(f"A random fruit from our list is: {random_fruit}")

    # `random.shuffle(list)` shuffles the items of a list in place.
    # "In place" means it modifies the original list directly and doesn't return
    # a new one.
    print(f"\nOriginal fruit list: {fruits}")
    random.shuffle(fruits)
    print(f"Shuffled fruit list: {fruits}")


    # --- Part 2: The `datetime` module ---
    # This module is essential for almost any application that needs to know
    # the current time or perform calculations with dates.

    print("\n--- Part 2: The `datetime` module ---")
    
    # `datetime.datetime.now()` returns a special DATETIME OBJECT that contains
    # the current date and time, down to the microsecond.
    current_time = datetime.datetime.now()
    print(f"The full datetime object is: {current_time}")
    
    # You can access individual components of the datetime object.
    print(f"  - Year: {current_time.year}")
    print(f"  - Month: {current_time.month}")
    print(f"  - Day: {current_time.day}")
    print(f"  - Hour: {current_time.hour}")
    print(f"  - Minute: {current_time.minute}")
    
    # The `.strftime()` method formats a datetime object into a readable string.
    # You pass it a "format code" string to specify how you want it to look.
    #  %Y = 4-digit year, %m = 2-digit month, %d = 2-digit day
    #  %H = 24-hour, %M = minute, %S = second
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Nicely formatted time: {formatted_time}")


    # --- Part 3: Beyond the Standard Library - pip and PyPI ---
    # The Python Standard Library is powerful, but it can't do everything.
    # What if you want to make HTTP requests to an API, process images, or
    # build a web server?
    #
    # The Python community has created hundreds of thousands of free, open-source
    # packages to solve these problems. These packages are stored in a central
    # repository called the PYTHON PACKAGE INDEX, or PyPI (pronounced "pie-pee-eye").
    #
    # So how do you get these packages from PyPI onto your computer?
    # You use PIP, the Package Installer for Python.
    #
    # PIP is a command-line tool that comes with your Python installation.
    # You run it from your terminal, NOT from within a Python script.
    #
    # EXAMPLE: One of the most famous and useful third-party packages is `requests`,
    # which is used to make web requests. To install it, you would open your
    # terminal/command prompt and type:
    #
    # `pip install requests`
    # (or `pip3 install requests` on some systems)
    #
    # Once installed, you can import and use it in your code just like a
    # standard library module:
    # `import requests`
    #
    # We will NOT be running pip in this script, as it's an external command.
    # But we will use it in future project lessons!

    print("\n--- Part 3: Understanding `pip` ---")
    print("Pip is a command-line tool for installing packages from PyPI.")
    print("To install a package, you open your terminal and run:")
    print("  `pip install package_name`")
    print("\nThis lesson does not install any packages, but it's a critical concept.")
    print("We will use pip to install 'requests' and 'matplotlib' in later lessons.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've learned how to harness the power of code written by others by using modules.

1.  A MODULE is a file of reusable Python code.
2.  The `import` statement makes a module's functionality available in your script.
3.  The PYTHON STANDARD LIBRARY is a vast collection of modules included with Python,
    like `random` (for random numbers) and `datetime` (for dates and times).
4.  To use something from a module, you use `module_name.function_or_variable`.
5.  For needs beyond the standard library, the PYTHON PACKAGE INDEX (PyPI) hosts
    hundreds of thousands of third-party packages.
6.  PIP is the command-line tool you use to install these packages from PyPI
    (e.g., `pip install requests`).

This concept of importing and combining modules is fundamental to modern software
development and allows you to build complex applications without reinventing the wheel.

HOW TO RUN THIS CODE:

1.  Save this file as `11_modules_and_pip.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 11_modules_and_pip.py`
'''