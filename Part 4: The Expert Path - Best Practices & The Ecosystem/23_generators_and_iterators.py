# -*- coding: utf-8 -*-
"""
Part 4, Lesson 23: Generators and Iterators

Author: dunamismax
Date: 06-15-2025

This file explains and demonstrates generators and iterators, focusing on
how they provide a memory-efficient way to work with large or infinite
sequences of data using the `yield` keyword.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So far, when we've needed a sequence of items, we've used a LIST. Lists are
fantastic, but they have one significant drawback: they store every single one
of their elements in memory at the same time.

What if you needed to process a sequence with one billion numbers? Or read a
log file that is 50 gigabytes in size? Creating a list to hold all that data
at once would likely crash your computer due to insufficient memory.

Python's elegant solution to this problem is the concept of ITERATORS and a
special, easy way to create them called GENERATORS.

An ITERATOR is an object that represents a stream of data. It doesn't hold all
the data in memory; instead, it knows how to produce the next item in the
sequence when you ask for it. A `for` loop is secretly using an iterator every
time you loop over a list, string, or dictionary.

A GENERATOR is a simple and powerful way to create an iterator. You write a
function that looks normal, but instead of using `return` to send back a final
result, you use the `yield` keyword to produce a series of values, one at a time.
'''

# We import the `sys` module to demonstrate memory usage later.
import sys

# --- Part 1: The Memory Problem with Lists ---
#
# Let's define a function that creates a list of numbers. This is the "old way"
# that we've been using so far. It works fine for small lists.

def create_number_list(n):
    """Creates a list containing all numbers from 0 to n-1."""
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


# --- Part 2: Creating a Generator with `yield` ---
#
# Now, let's create a GENERATOR FUNCTION. It looks almost identical, but notice
# the `yield` keyword instead of `append` and `return`.

def generate_numbers(n):
    """A generator function that yields numbers from 0 to n-1."""
    # This function doesn't store a list. It just keeps track of its current
    # position in the loop.
    for i in range(n):
        # The `yield` keyword is the magic here. It does three things:
        # 1. It produces the value (`i`) for the caller to use.
        # 2. It PAUSES the function's execution right here.
        # 3. It saves the function's state (the current value of `i`).
        # When asked for the next item, it resumes from this exact spot.
        yield i


# The main execution block starts here.
if __name__ == "__main__":

    print("--- Part 1: Demonstrating Memory Usage ---")
    
    # Let's create a list of 100,000 numbers.
    list_of_nums = create_number_list(100000)
    
    # And now, let's create a generator for the same range.
    # Notice that calling a generator function doesn't actually run the code inside.
    # It immediately returns a special GENERATOR OBJECT.
    generator_of_nums = generate_numbers(100000)
    
    print(f"Type of list_of_nums: {type(list_of_nums)}")
    print(f"Type of generator_of_nums: {type(generator_of_nums)}")
    
    # Now for the crucial difference: memory.
    # `sys.getsizeof()` gives the size of an object in bytes.
    # The list has to store all 100,000 integers in memory.
    # The generator object is tiny; it only needs to store its current state.
    list_mem = sys.getsizeof(list_of_nums)
    gen_mem = sys.getsizeof(generator_of_nums)
    
    print(f"\nMemory used by list of 100,000 numbers: {list_mem} bytes")
    print(f"Memory used by generator object:          {gen_mem} bytes")
    print(f"The list uses over {list_mem // gen_mem} times more memory!")
    

    # --- Part 3: Using a Generator ---
    #
    # Even though a generator isn't a list, you can use it in a `for` loop
    # in the exact same way. The `for` loop automatically handles asking the
    # generator for the next item until it's exhausted.
    
    print("\n--- Part 3: Looping Over a Generator ---")
    print("Summing numbers from a generator (first 10 shown):")
    
    # We create a new, smaller generator for this example.
    small_generator = generate_numbers(10)
    
    total = 0
    for number in small_generator:
        # In each iteration, a new number is generated just-in-time.
        # It's not stored anywhere after the loop moves on.
        print(f"  Yielded: {number}")
        total += number
    print(f"Sum of numbers from 0-9 is: {total}")
    

    # --- Part 4: The Iterator Protocol (`next()`) ---
    #
    # How does the `for` loop actually work? Under the hood, it's using the
    # built-in `next()` function on the iterator. Let's do it manually.
    
    print("\n--- Part 4: Using next() Manually ---")
    
    manual_gen = generate_numbers(3)
    
    # Calling `next()` on the generator resumes its execution until it hits `yield`.
    print(f"First call to next():  {next(manual_gen)}")  # Yields 0 and pauses.
    print(f"Second call to next(): {next(manual_gen)}") # Resumes, yields 1, and pauses.
    print(f"Third call to next():  {next(manual_gen)}")  # Resumes, yields 2, and pauses.
    
    # What happens if we call it again? The generator's loop is finished.
    # It signals this by raising a `StopIteration` exception. The `for` loop
    # listens for this exception to know when to end.
    try:
        next(manual_gen)
    except StopIteration:
        print("Fourth call to next() raised StopIteration, as expected.")


    # --- Part 5: Generator Expressions ---
    #
    # Remember LIST COMPREHENSIONS from Lesson 17?
    # `my_list = [x * x for x in range(5)]`
    # Python provides a similarly concise syntax for creating generators, called
    # a GENERATOR EXPRESSION. You just replace the square brackets `[]` with
    # parentheses `()`.
    
    print("\n--- Part 5: Generator Expressions ---")
    
    # This is a generator expression. It creates a generator object without
    # needing to write a full `def` function. It's memory-efficient.
    squares_generator = (x * x for x in range(5))
    
    print(f"Object created by expression: {squares_generator}")
    
    # We can loop over it just like any other generator.
    print("Squares from the generator expression:")
    for square in squares_generator:
        print(f"  {square}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just learned about generators, a key feature for writing efficient and
scalable Python code.

1.  Generators provide a memory-efficient way to create ITERATORS, which are
    objects that produce a sequence of items one by one.
2.  They are created with a GENERATOR FUNCTION, which uses the `yield` keyword
    instead of `return`.
3.  `yield` pauses the function, provides a value, and saves its state, ready
    to resume on the next call.
4.  Generators are used when dealing with very large datasets, streams of data,
    or potentially infinite sequences, where storing everything in a list would
    be impossible or wasteful.
5.  A GENERATOR EXPRESSION `(item for item in iterable)` is a concise, inline
    syntax for creating simple generators, similar to a list comprehension.

This concept is fundamental to advanced Python and is used extensively in data
science, web development, and systems programming.

HOW TO RUN THIS CODE:

1.  Save this file as `23_generators_and_iterators.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 23_generators_and_iterators.py`
'''