# -*- coding: utf-8 -*-
"""
Part 1, Lesson 6: Lists: The Python Workhorse

Author: dunamismax
Date: 06-15-2025

This file introduces the list data structure. It covers how to create,
index, slice, and modify lists, as well as demonstrating common
list methods like .append() and .pop().
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Lesson 6! You've learned about storing single pieces of data in
variables. But what if you need to store a collection of items, like a list of
groceries, a roster of players, or a series of steps in a recipe?

For this, we use a LIST.

A LIST in Python is an ORDERED collection of items. It is arguably the most
fundamental and versatile data structure in the language. You can think of it
as a container that holds multiple values in a specific sequence.

Key properties of lists:
- They are ORDERED: The items have a defined sequence that does not change.
- They are MUTABLE: You can change, add, and remove items after the list has been created.
- They can contain DUPLICATE items.
- They can contain items of DIFFERENT data types.
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: Creating a List ---
    # You create a list by placing items inside square brackets `[]`,
    # separated by commas.

    print("--- Part 1: Creating Lists ---")
    
    # A list of strings
    chores = ["take out the trash", "do the dishes", "walk the dog"]
    print(f"My list of chores: {chores}")

    # A list of numbers
    prime_numbers = [2, 3, 5, 7, 11, 13]
    print(f"Some prime numbers: {prime_numbers}")
    
    # A list can be empty, which is useful when you want to add items later.
    empty_list = []
    print(f"An empty list: {empty_list}")


    # --- Part 2: Accessing Items with Indexing ---
    # You can get a single item from a list using its position, or INDEX.
    #
    # CRITICAL CONCEPT: Python uses ZERO-BASED INDEXING. This means the first
    # item is at index 0, the second at index 1, and so on.
    
    print("\n--- Part 2: Accessing Items by Index ---")
    
    # Let's use our `chores` list again.
    # chores = ["take out the trash", "do the dishes", "walk the dog"]
    # Indices:        0                    1                2
    
    first_chore = chores[0]
    print(f"The first chore (at index 0) is: '{first_chore}'")
    
    second_chore = chores[1]
    print(f"The second chore (at index 1) is: '{second_chore}'")

    # NEGATIVE INDEXING: You can also access items from the end of the list.
    # -1 refers to the last item, -2 to the second-to-last, and so on.
    last_chore = chores[-1]
    print(f"The last chore (at index -1) is: '{last_chore}'")


    # --- Part 3: Slicing - Getting a Sub-List ---
    # SLICING lets you get a portion of a list, which results in a new list.
    # The syntax is `list[start:stop]`.
    # The `start` index is included, but the `stop` index is NOT included.

    print("\n--- Part 3: Slicing a List ---")
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    print(f"Original list of letters: {letters}")
    
    # Get items from index 1 up to (but not including) index 4
    slice1 = letters[1:4] # This will get items at index 1, 2, and 3
    print(f"letters[1:4] results in: {slice1}")
    
    # If you omit the start index, it defaults to the beginning (index 0).
    slice2 = letters[:3] # Get items from the start up to index 3
    print(f"letters[:3] results in: {slice2}")

    # If you omit the stop index, it defaults to the very end of the list.
    slice3 = letters[2:] # Get items from index 2 to the end
    print(f"letters[2:] results in: {slice3}")


    # --- Part 4: Modifying a List (Mutability) ---
    # Because lists are MUTABLE, you can change their contents directly.
    # You can change an item by accessing its index and assigning a new value.

    print("\n--- Part 4: Modifying a List ---")
    print(f"Original chores list: {chores}")
    
    # Let's say we already did the dishes and need to do laundry instead.
    chores[1] = "do the laundry"
    print(f"Modified chores list: {chores}")


    # --- Part 5: Common and Useful List Methods ---
    # A METHOD is a function that belongs to an object (in this case, a list).
    
    print("\n--- Part 5: Common List Methods ---")
    
    # `.append()` adds an item to the VERY END of the list.
    print(f"Chores before appending: {chores}")
    chores.append("clean my room")
    print(f"Chores after appending: {chores}")
    
    # `.pop()` removes the item at the end of the list and RETURNS it.
    # This is useful if you want to use the removed item.
    just_finished_chore = chores.pop()
    print(f"The chore I just finished (by using .pop()) was: '{just_finished_chore}'")
    print(f"The remaining chores list: {chores}")
    
    # You can also provide an index to `.pop()` to remove an item from a
    # specific position. Let's remove "take out the trash" (at index 0).
    urgent_chore = chores.pop(0)
    print(f"I just handled the urgent chore at index 0: '{urgent_chore}'")
    print(f"Final list of chores: {chores}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you were introduced to Python's workhorse data structure, the LIST.
1.  A LIST is an ORDERED, MUTABLE collection of items, created with `[]`.
2.  Python uses ZERO-BASED INDEXING to access items, where the first item is at
    index `[0]` and the last is at `[-1]`.
3.  SLICING (`list[start:stop]`) creates a new sub-list from your list.
4.  Because lists are MUTABLE, you can change them in-place, for example by
    reassigning an item at a specific index (`my_list[i] = new_value`).
5.  Common methods like `.append(item)` add to the end of a list, and `.pop()`
    removes from the end of a list.

HOW TO RUN THIS CODE:

1.  Save this file as `6_lists_the_python_workhorse.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 6_lists_the_python_workhorse.py`
'''