# -*- coding: utf-8 -*-
"""
Part 3, Lesson 20: Lambdas and Functional Tools

Author: dunamismax
Date: 06-15-2025

This file introduces concepts from functional programming, including
lambda functions (anonymous functions) and the powerful built-in
functions `map()` and `filter()`.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So far, we have been programming in what is mostly an "imperative" style: we
write a series of commands that the computer executes in order. There are other
programming paradigms, and one influential one is FUNCTIONAL PROGRAMMING.

A core idea in functional programming is treating functions as first-class
citizens. This means a function is just another piece of data, like a number
or a string. You can pass a function as an argument to another function, or
have a function return another function.

Python isn't a purely functional language, but it incorporates many powerful
ideas from this paradigm. In this lesson, we'll explore three of them:

1.  LAMBDA FUNCTIONS: Tiny, anonymous, one-line functions that you can create
    on the fly without a full `def` statement.

2.  `map()`: A function that takes another function and applies it to every
    item in a list (or other iterable).

3.  `filter()`: A function that takes another function and uses it to "filter"
    items out of a list, keeping only those that match a condition.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: Lambda Functions ---
    # Sometimes you need a small, simple function for a single, brief task.
    # Writing a full `def` block can feel overly formal. For this, Python
    # gives us the `lambda` keyword.

    # A LAMBDA function is an anonymous, single-expression function.
    # The syntax is: `lambda arguments: expression`

    print("--- Part 1: Lambda Functions ---")

    # Regular function definition:
    def double(x):
        return x * 2

    print(f"Using a regular function: double(5) = {double(5)}")

    # The equivalent lambda function:
    # We assign the lambda to a variable to give it a name, but often they are
    # used directly without being assigned to anything.
    double_lambda = lambda x: x * 2

    print(f"Using a lambda function: double_lambda(5) = {double_lambda(5)}")

    # Lambdas can have multiple arguments.
    add_lambda = lambda x, y: x + y
    print(f"A lambda with two arguments: add_lambda(3, 4) = {add_lambda(3, 4)}")
    
    # The real power of lambdas comes when they are used as quick, disposable
    # arguments to other functions, as we'll see next.


    # --- Part 2: The `map()` Function ---
    # The `map()` function applies a given function to every item in an iterable.
    # Its syntax is: `map(function_to_apply, iterable)`

    print("\n--- Part 2: The map() Function ---")
    
    numbers = [1, 2, 3, 4, 5]
    
    # Let's say we want to double every number in our list.
    # We could use a list comprehension (which is often preferred for simple cases):
    doubled_comp = [x * 2 for x in numbers]
    print(f"Doubling with a list comprehension: {doubled_comp}")
    
    # Or, we can use `map()`. We pass it our `double` function and the list.
    # IMPORTANT: `map()` returns a MAP OBJECT, not a list. A map object is an
    # iterator, which is a memory-efficient way of generating values one by one.
    # To see the results, we must convert it to a list.
    doubled_map_object = map(double, numbers)
    doubled_map_list = list(doubled_map_object)
    
    print(f"Doubling with map() and a def function: {doubled_map_list}")
    
    # The most common pattern is to use `map()` with a `lambda` function directly.
    # This avoids having to define a separate function just for this one operation.
    doubled_map_lambda = list(map(lambda x: x * 2, numbers))
    print(f"Doubling with map() and a lambda: {doubled_map_lambda}")


    # --- Part 3: The `filter()` Function ---
    # The `filter()` function builds an iterator from elements of an iterable
    # for which a function returns `True`.
    # Syntax: `filter(function_that_returns_bool, iterable)`

    print("\n--- Part 3: The filter() Function ---")
    
    # Let's get only the even numbers from our list.
    # With a list comprehension:
    even_comp = [x for x in numbers if x % 2 == 0]
    print(f"Filtering evens with a comprehension: {even_comp}")
    
    # To use `filter()`, we need a function that returns True or False.
    def is_even(n):
        return n % 2 == 0
        
    # Like `map()`, `filter()` also returns an iterator (a filter object).
    even_filter_object = filter(is_even, numbers)
    even_filter_list = list(even_filter_object)
    print(f"Filtering with filter() and a def function: {even_filter_list}")
    
    # And again, the most common pattern is to use a lambda.
    even_filter_lambda = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Filtering with filter() and a lambda: {even_filter_lambda}")


    # --- Part 4: Chaining Functional Tools ---
    # You can combine these tools to create powerful, readable data pipelines.
    
    print("\n--- Part 4: Chaining map() and filter() ---")
    
    # Task: From our list of numbers, find the even ones, and then square them.
    
    # 1. Filter the list to get only the even numbers.
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    
    # 2. Map a squaring function onto the result of the filter.
    squared_evens = list(map(lambda x: x * x, even_numbers))
    
    print(f"Original numbers: {numbers}")
    print(f"Result of filtering for evens, then squaring: {squared_evens}")
    
'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations on completing Part 3! You've dipped your toes into the world
of functional programming in Python.

1.  LAMBDA FUNCTIONS (`lambda arguments: expression`) are small, anonymous
    functions that are perfect for short-term operations, especially when
    passed as arguments to other functions.

2.  `map(function, iterable)` applies a function to every item in an iterable.
    It returns a memory-efficient iterator, which you usually convert to a list
    with `list()`.

3.  `filter(function, iterable)` creates an iterator containing only the items
    from an iterable for which the function returns `True`.

While a list comprehension is often the most "Pythonic" choice for simple
mapping and filtering, `map()` and `filter()` are powerful tools, especially
when dealing with more complex functions or when you prefer a more explicitly
functional style.

You are now equipped with advanced data handling techniques and are ready to
tackle Part 4, where we'll focus on professional best practices.

HOW TO RUN THIS CODE:

1.  Save this file as `20_lambdas_and_functional_tools.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 20_lambdas_and_functional_tools.py`
'''