# -*- coding: utf-8 -*-
"""
Part 3, Lesson 17: List and Dict Comprehensions

Author: dunamismax
Date: 06-15-2025

This file teaches a powerful and "Pythonic" feature for creating
lists and dictionaries concisely: comprehensions. It shows how they
are often more readable and efficient than traditional loops.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So far, when we've needed to create a new list or dictionary based on an
existing one, we've used a `for` loop. We initialize an empty list, loop
through the source data, perform some action, and append the result on each
iteration. This works perfectly fine, but it's a bit verbose.

Python, a language that values readability and elegance, provides a more
concise and often faster way to do this: COMPREHENSIONS.

A COMPREHENSION is a compact way to create a new sequence (like a list or
dictionary) by running an expression on each item in another sequence. It's
like a `for` loop, a condition, and an assignment all in one elegant line.

Mastering comprehensions is a key step toward writing clean, professional,
and "Pythonic" code.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: The Old Way - Building a List with a Loop ---
    # Let's say we have a list of numbers and we want a new list containing
    # the square of each number. Here's how we've done it so far.
    
    print("--- Part 1: The Standard Loop Method ---")
    
    numbers = [1, 2, 3, 4, 5, 6]
    squared_numbers = []  # 1. Initialize an empty list
    
    for number in numbers:  # 2. Loop through the source list
        squared_numbers.append(number * number)  # 3. Append the result
        
    print(f"Original numbers: {numbers}")
    print(f"Squared (with a loop): {squared_numbers}")
    print("This requires 3 lines of code for a simple transformation.")


    # --- Part 2: The New Way - List Comprehension ---
    # A LIST COMPREHENSION does the exact same thing in a single, readable line.
    # The syntax is: `new_list = [expression for item in iterable]`

    print("\n--- Part 2: List Comprehension ---")
    
    # Here is the list comprehension version of the code above.
    squared_comp = [number * number for number in numbers]
    
    # Let's break that down:
    # [            ...           ]  # The brackets indicate we are creating a list.
    #  number * number              # This is the EXPRESSION to execute for each item.
    #                  for number   # This is the loop variable.
    #                           in numbers  # This is the source iterable.
    
    print(f"Squared (with comprehension): {squared_comp}")
    print("This does the same thing in one elegant line!")


    # --- Part 3: List Comprehension with a Condition ---
    # Comprehensions can also include an `if` condition to filter items.
    # The syntax is: `new_list = [expression for item in iterable if condition]`
    
    print("\n--- Part 3: List Comprehension with a Condition ---")
    
    # Let's create a new list containing only the squares of the EVEN numbers.
    
    # The old way with a loop:
    even_squares_loop = []
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            even_squares_loop.append(number * number)
    
    print(f"Even squares (with a loop): {even_squares_loop}")
    
    # The new way with a comprehension:
    even_squares_comp = [number * number for number in numbers if number % 2 == 0]
    
    # Breakdown:
    # [number * number for number in numbers ... ] # Same as before...
    #                                      if number % 2 == 0 # ...but only if this condition is True.
    
    print(f"Even squares (with comprehension): {even_squares_comp}")


    # --- Part 4: Dictionary Comprehensions ---
    # This powerful idea isn't limited to lists. You can also create dictionaries.
    # The syntax is similar, but uses curly braces `{}` and a key-value pair.
    # `new_dict = {key_expression: value_expression for item in iterable}`
    
    print("\n--- Part 4: Dictionary Comprehension ---")
    
    fruits = ["apple", "banana", "cherry"]
    
    # Let's create a dictionary where the fruit name is the key
    # and the length of the name is the value.
    
    # The old way with a loop:
    fruit_lengths_loop = {}
    for fruit in fruits:
        fruit_lengths_loop[fruit] = len(fruit)
        
    print(f"Fruit lengths (with a loop): {fruit_lengths_loop}")

    # The new way with a DICTIONARY COMPREHENSION:
    fruit_lengths_comp = {fruit: len(fruit) for fruit in fruits}
    
    # Breakdown:
    # {          ...          } # The curly braces indicate a dictionary.
    #  fruit: len(fruit)        # The key: value pair to create.
    #                      for fruit in fruits # The loop.

    print(f"Fruit lengths (with comprehension): {fruit_lengths_comp}")


    # --- Part 5: Dictionary Comprehension with a Condition ---
    # Just like list comprehensions, you can add an `if` clause.
    
    print("\n--- Part 5: Dictionary Comprehension with a Condition ---")
    
    student_scores = {
        "Alice": 88,
        "Bob": 59,
        "Charlie": 95,
        "David": 67
    }
    
    # Let's create a new dictionary of only the students who passed (score > 60).
    passing_students = {name: score for name, score in student_scores.items() if score > 60}
    
    print(f"Original scores: {student_scores}")
    print(f"Passing students only (with comprehension): {passing_students}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just learned one of the most beloved features of the Python language.
Comprehensions are a powerful tool for transforming and filtering data.

1.  A COMPREHENSION is a concise, single-line syntax for creating a new list
    or dictionary from an existing iterable.

2.  LIST COMPREHENSION syntax:
    `[expression for item in iterable]`
    `[expression for item in iterable if condition]`

3.  DICTIONARY COMPREHENSION syntax:
    `{key_expr: val_expr for item in iterable}`
    `{key_expr: val_expr for item in iterable if condition}`

4.  Why use them? They are often more readable and can be more performant than
    an equivalent `for` loop. They are a hallmark of idiomatic, "Pythonic" code.

From now on, whenever you find yourself writing a `for` loop just to build a
new list or dictionary, ask yourself: "Can I use a comprehension here?" The
answer will often be yes!

HOW TO RUN THIS CODE:

1.  Save this file as `17_list_and_dict_comprehensions.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 17_list_and_dict_comprehensions.py`
'''