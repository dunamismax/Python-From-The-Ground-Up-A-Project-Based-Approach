# -*- coding: utf-8 -*-
"""
Part 4, Lesson 24: Testing with pytest

Author: dunamismax
Date: 06-15-2025

This file introduces the concept of automated testing using the `pytest`
library. It demonstrates how to write simple test functions to verify
that our code works as expected.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

As your programs grow larger and more complex, how can you be sure that a new
change in one part of the code doesn't accidentally break something else?
Manually testing every feature after every single change is slow, tedious,
and prone to human error.

The professional solution is AUTOMATED TESTING.

AUTOMATED TESTING is the practice of writing code to test your other code. You
define a set of "test cases"—specific inputs and their expected outputs—and run
a testing framework to automatically execute them and report any failures.

This provides a safety net, giving you confidence that your code is correct and
allowing you to refactor and add new features without fear.

PYTEST: THE PYTHON TESTING FRAMEWORK
While Python has a built-in `unittest` module, the most popular, powerful, and
developer-friendly testing framework in the ecosystem is `pytest`. It allows you
to write simple, readable tests with minimal boilerplate code.

--- SETUP: THIS LESSON REQUIRES `pytest` ---

You will need to install `pytest` into a virtual environment.

1.  Create a new project folder and navigate into it:
    `mkdir testing_project && cd testing_project`

2.  Create and activate a virtual environment:
    `python -m venv venv`
    `source venv/bin/activate` (or `.\\venv\\Scripts\\activate` on Windows)

3.  Install pytest:
    `pip install pytest`

4.  Save your dependencies:
    `pip freeze > requirements.txt`

5.  This lesson is split into TWO files. Create both of them inside your
    `testing_project` folder:
    a) `main_code.py`: The file containing the functions we want to test.
    b) `test_main_code.py`: The file containing the tests for our functions.

    This separation is a standard convention. Keep your application code
    separate from your test code.

For this lesson, this file (`24_testing_with_pytest.py`) acts as the guide.
The code you will actually *run* with pytest will be in the two files described
above.
'''

# --- Part 1: The Code We Want to Test ---
#
# Imagine we have a project with a file named `main_code.py`. This file contains
# a few utility functions that we want to ensure are always working correctly.
#
# ======================== FILE: main_code.py ========================
#
# # -*- coding: utf-8 -*-
# """Functions to be tested."""
#
# def add(a, b):
#     """Returns the sum of two numbers."""
#     return a + b
#
# def is_even(number):
#     """Returns True if a number is even, False otherwise."""
#     return number % 2 == 0
#
# class Account:
#     """A simple bank account class."""
#     def __init__(self, start_balance=0):
#         if start_balance < 0:
#             # We can use `raise` to signal an error condition.
#             # pytest can test for these, too!
#             raise ValueError("Initial balance cannot be negative.")
#         self._balance = start_balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive.")
#         self._balance += amount
#
# ====================================================================


# --- Part 2: Writing the Test File with `pytest` ---
#
# Now we create our test file. `pytest` has simple but powerful discovery rules:
# 1. It looks for files named `test_*.py` or `*_test.py`.
# 2. Inside those files, it looks for functions prefixed with `test_`.
#
# Each `test_` function should test one specific behavior. Inside the function,
# you use the plain `assert` keyword. An ASSERTION is a statement that a certain
# condition must be true. If it is, the test passes silently. If it's false,
# the test fails and `pytest` will report it.
#
# ====================== FILE: test_main_code.py =====================
#
# # -*- coding: utf-8 -*-
# """Tests for our main_code.py functions."""
#
# # We need to import the code we want to test.
# from main_code import add, is_even, Account
# import pytest # We need pytest to test for exceptions.
#
# # A test for our `add` function.
# def test_add_positive_numbers():
#     # The assertion checks if the actual result matches the expected result.
#     assert add(2, 3) == 5
#
# def test_add_negative_numbers():
#     assert add(-1, -1) == -2
#
# # A test for our `is_even` function.
# def test_is_even_with_even_number():
#     assert is_even(10) is True
#
# def test_is_even_with_odd_number():
#     assert is_even(7) is False
#
# # Testing our Account class
# def test_account_initial_balance():
#     acc = Account(50)
#     assert acc.get_balance() == 50
#
# def test_account_deposit():
#     acc = Account(10)
#     acc.deposit(20)
#     assert acc.get_balance() == 30
#
# # How to test for expected errors? Use `pytest.raises`.
# # This is called a "context manager" (like `with open(...)`).
# # The test passes ONLY if a `ValueError` is raised inside the `with` block.
# def test_account_negative_initial_balance_raises_error():
#     with pytest.raises(ValueError):
#         Account(-10)
#
# def test_account_negative_deposit_raises_error():
#     acc = Account(100)
#     with pytest.raises(ValueError):
#         acc.deposit(-20)
#
# ====================================================================


# --- Part 3: Running the Tests ---
#
# Running the tests is the easiest part.
#
# 1.  Make sure you are in your project directory (`testing_project`) in the terminal.
# 2.  Make sure your virtual environment is active.
# 3.  Simply run the command:
#
#     `pytest`
#
# `pytest` will automatically discover your `test_main_code.py` file, run all the
# functions inside it that start with `test_`, and give you a detailed report.
#
# A passing run will look something like this:
#
#   `===================== test session starts =====================`
#   `...`
#   `collected 7 items`
#
#   `test_main_code.py .......                                [100%]`
#
#   `====================== 7 passed in 0.01s ======================`
#
# If a test fails (e.g., if we changed `add(2, 3)` to return 6), the output
# would clearly show the failure, what was expected, and what was actually returned.
# This makes debugging incredibly fast.

if __name__ == "__main__":
    # This main file is just a guide. To perform the lesson, you need to create
    # the two files (`main_code.py` and `test_main_code.py`) and run `pytest`
    # from your terminal.

    print("--- Introduction to Automated Testing with pytest ---")
    print("\nThis file serves as the documentation for the lesson.")
    print("To complete this lesson, you must perform the following steps:")
    print("\n1. Create a project folder and set up a virtual environment.")
    print("2. Install `pytest` using `pip install pytest`.")
    print("3. Create a file named `main_code.py` with the functions to be tested.")
    print("4. Create a second file named `test_main_code.py` with the test functions.")
    print("5. Open your terminal in the project folder.")
    print("6. Run the command `pytest` to execute your tests.")
    print("\nReview the contents of this file to understand how to write the tests.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just been introduced to the fundamental practice of automated testing,
a cornerstone of modern, professional software development.

1.  AUTOMATED TESTS are code that tests your application code, providing a
    safety net against bugs and regressions.
2.  `pytest` is a popular and powerful testing framework for Python.
3.  `pytest` discovers test files (`test_*.py`) and test functions (`test_*()`)
    automatically.
4.  The `assert` keyword is used to check if a condition is true. If not, the
    test fails.
5.  Good tests are small, fast, and test only one specific behavior.
6.  You can test for expected errors using the `with pytest.raises(ExceptionType):`
    context manager.
7.  Keeping tests separate from application code is standard practice.

Writing tests may seem like extra work at first, but it saves an enormous
amount of time and stress in the long run by catching bugs early.

HOW TO "RUN" THIS LESSON:

1.  Follow the setup instructions to create a project folder with a virtual
    environment and install `pytest`.
2.  Create the `main_code.py` file and copy the example code into it.
3.  Create the `test_main_code.py` file and copy the test code into it.
4.  From your terminal (with the venv activated), run the command `pytest`.
5.  Experiment! Try making a test fail by changing the `main_code.py` file and
    see how `pytest` reports the error.
'''