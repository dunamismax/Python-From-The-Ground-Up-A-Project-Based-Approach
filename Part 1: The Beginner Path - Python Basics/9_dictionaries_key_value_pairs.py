# -*- coding: utf-8 -*-
"""
Part 1, Lesson 9: Dictionaries: Key-Value Pairs

Author: dunamismax
Date: 06-15-2025

This file introduces the dictionary data structure. It covers how to
create dictionaries, access, add, modify, and remove data using keys,
and how to loop through them effectively.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to the final lesson of Part 1! So far, we've used lists to store
ordered collections of items, which we access using a numerical index (0, 1, 2...).

But what if we want to store data and access it with a custom label instead of
a number? Imagine a contact card: you wouldn't look up a person's email at
"contact index 2"; you'd look it up by the label "email".

For this, Python gives us the DICTIONARY.

A DICTIONARY is an UNORDERED (in older Python versions) collection of data stored as
KEY-VALUE PAIRS. In modern Python (3.7+), dictionaries are ordered by insertion.
Think of it like a real-world dictionary where each word (the KEY) has a
corresponding definition (the VALUE).

Key properties of dictionaries:
- They are MUTABLE: You can change, add, and remove key-value pairs.
- Keys must be UNIQUE. You cannot have two identical keys in the same dictionary.
- Keys must be IMMUTABLE types (like strings, numbers, or tuples). You cannot use a list as a key.
- Values can be of any data type (strings, numbers, lists, even other dictionaries!).
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: Creating a Dictionary ---
    # You create a dictionary using curly braces `{}`. Each item is a pair
    # written as `key: value`, and pairs are separated by commas.

    print("--- Part 1: Creating a Dictionary ---")
    
    # Let's create a dictionary to store information about a student.
    # The keys are strings ("name", "age", "major"), and the values are
    # a string, an integer, and another string.
    student = {
        "name": "Alice",
        "age": 21,
        "major": "Computer Science"
    }
    
    print(f"Our student dictionary: {student}")


    # --- Part 2: Accessing Values Using Keys ---
    # You don't use a numerical index like in lists. Instead, you use the key
    # inside square brackets `[]` to get its corresponding value.

    print("\n--- Part 2: Accessing Values ---")

    student_name = student["name"]
    print(f"The student's name is: {student_name}")
    
    student_age = student["age"]
    print(f"The student's age is: {student_age}")
    
    # IMPORTANT: If you try to access a key that doesn't exist, your program
    # will raise an error (a `KeyError`). This is a common bug!
    # For example, `student["gpa"]` would cause a crash right now.


    # --- Part 3: Safe Access with the `.get()` Method ---
    # To avoid errors from missing keys, it's safer to use the `.get()` method.
    # If the key exists, it returns the value. If it doesn't, it returns `None`
    # (a special Python value representing nothing) instead of crashing.

    print("\n--- Part 3: Safe Access with .get() ---")
    
    student_major = student.get("major")
    print(f"Getting major with .get(): {student_major}")
    
    # The 'gpa' key does not exist, but the program doesn't crash.
    student_gpa = student.get("gpa")
    print(f"Getting GPA with .get(): {student_gpa}") # This will print 'None'
    
    # You can also provide a default value to return if the key is not found.
    student_gpa_default = student.get("gpa", "Not Available")
    print(f"Getting GPA with a default value: {student_gpa_default}")


    # --- Part 4: Modifying and Adding to a Dictionary ---
    # Dictionaries are mutable, so you can easily change them.
    
    print("\n--- Part 4: Modifying a Dictionary ---")
    
    # To change an existing value, just assign a new value to the key.
    print(f"Original major: {student['major']}")
    student["major"] = "Electrical Engineering"
    print(f"Updated major: {student['major']}")
    
    # To add a new key-value pair, assign a value to a new key.
    print(f"\nDictionary before adding: {student}")
    student["is_enrolled"] = True
    print(f"Dictionary after adding 'is_enrolled': {student}")


    # --- Part 5: Removing Items ---
    # You can use the `del` keyword to remove a key-value pair.
    
    print("\n--- Part 5: Removing an Item ---")
    
    print(f"Dictionary before deleting 'age': {student}")
    del student["age"]
    print(f"Dictionary after deleting 'age': {student}")


    # --- Part 6: Looping Through a Dictionary ---
    # A common task is to go through all the key-value pairs.
    
    print("\n--- Part 6: Looping through a Dictionary ---")
    
    # The most "Pythonic" way to loop is using the `.items()` method.
    # It gives you both the key and the value in each iteration.
    print("Using .items() to get keys and values:")
    for key, value in student.items():
        print(f"  Key: '{key}' -> Value: '{value}'")
        
'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations on completing Part 1! You've just learned about dictionaries,
one of the most powerful and commonly used data types in Python.

1.  A DICTIONARY stores data as KEY-VALUE PAIRS, created with `{}`.
2.  Values are accessed using their unique, immutable KEY inside `[]`, not a
    numerical index.
3.  The `.get(key, default)` method is a safe way to access values without
    risking errors from missing keys.
4.  Dictionaries are MUTABLE: you can add, change, and delete pairs.
5.  The best way to loop through a dictionary is with the `.items()` method,
    which provides both the key and the value on each pass.

You now have a solid foundation in the absolute basics of Python! In Part 2,
we'll start building more complex and useful tools.

HOW TO RUN THIS CODE:

1.  Save this file as `9_dictionaries_key_value_pairs.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 9_dictionaries_key_value_pairs.py`
'''