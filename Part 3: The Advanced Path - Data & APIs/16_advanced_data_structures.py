# -*- coding: utf-8 -*-
"""
Part 3, Lesson 16: Advanced Data Structures

Author: dunamismax
Date: 06-15-2025

This file introduces two important data structures beyond lists and
dictionaries: tuples and sets. It explains their unique properties
and when to use each one.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Part 3! You have a strong grasp of Python's workhorses: lists for
ordered collections and dictionaries for key-value pairs. Now it's time to
add two more specialized tools to your toolkit: TUPLES and SETS.

While lists and dictionaries can solve most problems, tuples and sets offer
specific advantages in certain situations, often leading to safer or more
efficient code.

- A TUPLE is like a list, but it's IMMUTABLE. Once you create it, you cannot
  change it. This is useful for data that should never be modified.

- A SET is a collection like a list, but it is UNORDERED and only stores
  UNIQUE items. This makes it incredibly fast for checking if an item exists
  in a collection and for removing duplicates.

Let's explore them.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: Tuples - Immutable Sequences ---
    # A TUPLE is an ordered collection of items, created with parentheses `()`.
    # The key difference from a list is that a tuple is IMMUTABLE, meaning its
    # contents cannot be changed after creation.

    print("--- Part 1: Tuples ---")
    
    # Let's define a tuple. It looks just like a list, but with `()` instead of `[]`.
    # This could represent a point in 2D space (x, y).
    point = (10, 20)
    
    print(f"Our point tuple: {point}")
    
    # Like lists, you can access elements by their index because tuples are ordered.
    x_coordinate = point[0]
    y_coordinate = point[1]
    print(f"X coordinate is {x_coordinate}, Y coordinate is {y_coordinate}")

    # THE MOST IMPORTANT PROPERTY: You cannot change a tuple.
    # If we try to assign a new value to an element, Python will raise a TypeError.
    # This is a good thing! It protects your data from being changed accidentally.
    
    # The following line is commented out because it would crash the program.
    # Uncomment it to see the error for yourself!
    # point[0] = 15  # <-- This will cause a TypeError: 'tuple' object does not support item assignment
    
    print("\nAttempting to change a tuple would cause a TypeError.")


    # --- Part 2: When to Use a Tuple ---
    # Use a tuple when you have a collection of items that should not change.
    
    print("\n--- Part 2: Use Cases for Tuples ---")
    
    # 1. For data that is logically constant, like days of the week or coordinates.
    days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(f"Days of the week tuple: {days_of_week}")

    # 2. As keys in a dictionary. Remember how dictionary keys must be immutable?
    #    A list cannot be a key, but a tuple can!
    #    Let's map coordinates (tuples) to city names (strings).
    city_locations = {
        (40.7128, -74.0060): "New York City",
        (34.0522, -118.2437): "Los Angeles"
    }
    print(f"Dictionary with tuple keys: {city_locations}")
    nyc_coordinates = (40.7128, -74.0060)
    print(f"The city at {nyc_coordinates} is {city_locations[nyc_coordinates]}.")


    # --- Part 3: Sets - Collections of Unique Items ---
    # A SET is an UNORDERED collection of UNIQUE elements.
    # You create them with curly braces `{}` (like dictionaries, but no colons)
    # or with the `set()` function.

    print("\n--- Part 3: Sets ---")
    
    # Let's create a list with duplicate numbers.
    numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"Original list with duplicates: {numbers_list}")
    
    # Now, let's convert it to a set. Notice the duplicates are automatically removed.
    numbers_set = set(numbers_list)
    print(f"Converted to a set (duplicates removed): {numbers_set}")
    
    # You can also create a set directly with `{}`.
    fruits_set = {"apple", "banana", "cherry"}
    print(f"A set of fruits: {fruits_set}")
    
    # You can add and remove items.
    fruits_set.add("orange")  # Add a new item
    fruits_set.add("apple")   # Adding an existing item does nothing
    print(f"After adding 'orange' and 'apple' again: {fruits_set}")
    
    fruits_set.remove("banana") # Removes the item. Raises a KeyError if not found.
    print(f"After removing 'banana': {fruits_set}")
    
    # Because sets are unordered, you CANNOT access elements by index.
    # The following line is commented out because it would cause a TypeError.
    # first_fruit = fruits_set[0] # <-- This will cause a TypeError
    
    
    # --- Part 4: Practical Set Operations ---
    # The real power of sets is in performing mathematical operations like
    # union, intersection, and difference. They are extremely efficient for this.

    print("\n--- Part 4: Set Operations ---")
    
    programmers = {"Alice", "Bob", "Charlie", "David"}
    designers = {"Charlie", "David", "Eve", "Frank"}
    
    print(f"Programmers: {programmers}")
    print(f"Designers:   {designers}")
    
    # UNION: All unique people from both sets. (Who is on either team?)
    # Can be done with the `|` operator or the `.union()` method.
    all_staff = programmers.union(designers)
    print(f"\nUnion (all staff): {all_staff}")
    
    # INTERSECTION: People who are in BOTH sets. (Who is both a programmer and designer?)
    # Can be done with the `&` operator or the `.intersection()` method.
    cross_functional = programmers & designers
    print(f"Intersection (cross-functional staff): {cross_functional}")
    
    # DIFFERENCE: People in the first set but NOT in the second. (Who are ONLY programmers?)
    # Can be done with the `-` operator or the `.difference()` method.
    only_programmers = programmers - designers
    print(f"Difference (programmers who are not designers): {only_programmers}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you've learned about two powerful, specialized data structures.

1.  TUPLES (created with `()`):
    - They are ORDERED, like lists.
    - They are IMMUTABLE, meaning you cannot change their contents after creation.
    - Use them for fixed collections of data (like coordinates) or as
      dictionary keys.

2.  SETS (created with `{}` or `set()`):
    - They are UNORDERED.
    - They only store UNIQUE elements, automatically discarding duplicates.
    - Use them to quickly check for membership, remove duplicates from a list,
      or perform mathematical set operations (UNION, INTERSECTION, DIFFERENCE).

Choosing the right data structure for the job is a key skill. While a list
can often work, using a tuple or a set can make your code's intent clearer,
safer, and more efficient.

HOW TO RUN THIS CODE:

1.  Save this file as `16_advanced_data_structures.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 16_advanced_data_structures.py`
'''