# -*- coding: utf-8 -*-
"""
Part 1, Lesson 4: Operators and Comparisons

Author: dunamismax
Date: 06-15-2025

This file explains and demonstrates the fundamental operators in Python.
It covers arithmetic, comparison, and logical operators, which are the
building blocks for performing calculations and making decisions in your code.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Lesson 4! Now that we know how to store data in variables, let's learn
how to operate on that data.

An OPERATOR is a special symbol that performs a specific operation on one or more
values (called operands). For example, the plus sign `+` is an operator that
performs the operation of addition.

We will explore three main types of operators:
1.  ARITHMETIC OPERATORS: For doing math (+, -, *, /).
2.  COMPARISON OPERATORS: For comparing values (==, !=, >, <).
3.  LOGICAL OPERATORS: For combining true/false values (and, or, not).
'''

# The main execution block starts here.
if __name__ == "__main__":

    # --- Part 1: Arithmetic Operators ---
    # These are the operators used for mathematical calculations.

    print("--- Part 1: Arithmetic Operators ---")
    a = 15
    b = 4

    # Addition (+)
    sum_result = a + b
    print(f"{a} + {b} = {sum_result}")

    # Subtraction (-)
    difference_result = a - b
    print(f"{a} - {b} = {difference_result}")

    # Multiplication (*)
    product_result = a * b
    print(f"{a} * {b} = {product_result}")

    # Division (/) - Standard division always results in a float.
    quotient_result = a / b
    print(f"{a} / {b} = {quotient_result}")
    
    print("\n--- More Arithmetic Operators ---")
    
    # Floor Division (//) - Divides and rounds DOWN to the nearest whole number.
    floor_result = a // b
    print(f"{a} // {b} = {floor_result} (Floor Division)")
    
    # Modulo (%) - Gives the REMAINDER of a division. This is extremely useful!
    # For example, to check if a number is even, you can see if `number % 2` is 0.
    remainder_result = a % b
    print(f"{a} % {b} = {remainder_result} (Remainder/Modulo)")
    
    # Exponentiation (**) - Raises a number to a power.
    power_result = 2 ** 3  # This means 2 * 2 * 2
    print(f"2 ** 3 = {power_result} (Exponent)")


    # --- Part 2: Comparison Operators ---
    # These operators compare two values and the result is always a BOOLEAN (`True` or `False`).
    
    print("\n--- Part 2: Comparison Operators ---")
    x = 10
    y = 5
    
    print(f"Our values are x = {x} and y = {y}\n")

    # Equal to (==)
    # IMPORTANT: `==` is for comparison. `=` is for assignment. A common beginner mistake!
    print(f"Is x equal to y?      (x == y)  -> {x == y}")
    
    # Not equal to (!=)
    print(f"Is x not equal to y?  (x != y)  -> {x != y}")
    
    # Greater than (>)
    print(f"Is x greater than y?  (x > y)   -> {x > y}")

    # Less than (<)
    print(f"Is x less than y?     (x < y)   -> {x < y}")

    # Greater than or equal to (>=)
    print(f"Is x >= 10?           (x >= 10) -> {x >= 10}")
    
    # Less than or equal to (<=)
    print(f"Is y <= 5?            (y <= 5)  -> {y <= 5}")


    # --- Part 3: Logical Operators ---
    # These operators are used to combine or invert boolean values.

    print("\n--- Part 3: Logical Operators ---")
    is_hot = True
    is_raining = False
    
    print(f"Values: is_hot = {is_hot}, is_raining = {is_raining}\n")
    
    # `and` - Returns `True` only if BOTH sides are `True`.
    # Should you wear shorts? Only if it's hot AND not raining.
    wear_shorts = is_hot and not is_raining
    print(f"Wear shorts? (is_hot and not is_raining) -> {wear_shorts}")
    
    # `or` - Returns `True` if AT LEAST ONE side is `True`.
    # Is it a complex weather day? If it's hot OR it's raining.
    complex_weather = is_hot or is_raining
    print(f"Complex weather? (is_hot or is_raining) -> {complex_weather}")
    
    # `not` - Inverts the boolean value.
    # `not True` becomes `False`. `not False` becomes `True`.
    print(f"The opposite of is_raining is: (not is_raining) -> {not is_raining}")
    
    # Combining them all:
    # A good day is when it's hot AND it is NOT raining.
    is_a_good_day = is_hot and (not is_raining)
    print(f"Is it a good day? -> {is_a_good_day}")


    # --- Part 4: Operator Precedence ---
    # Python follows a standard order of operations, similar to PEMDAS in math.
    # Exponents first, then multiplication/division, then addition/subtraction.
    
    print("\n--- Part 4: Operator Precedence ---")
    
    # Multiplication happens before addition.
    result1 = 10 + 2 * 3  # This is 10 + 6
    print(f"10 + 2 * 3 = {result1}")
    
    # You can use parentheses `()` to control the order, just like in math.
    # This is also great for making your code easier to read.
    result2 = (10 + 2) * 3 # This is 12 * 3
    print(f"(10 + 2) * 3 = {result2}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

In this lesson, you've learned about the core operators in Python:
1.  ARITHMETIC OPERATORS (`+`, `-`, `*`, `/`, `//`, `%`, `**`) perform mathematical
    calculations on numbers.
2.  The `+` operator can also be used for STRING CONCATENATION (joining strings).
3.  COMPARISON OPERATORS (`==`, `!=`, `>`, `<`, `>=`, `<=`) compare two values and
    always result in a BOOLEAN (`True` or `False`).
4.  LOGICAL OPERATORS (`and`, `or`, `not`) are used to combine or invert
    Boolean values, which is essential for making decisions.
5.  Python has a defined order of OPERATOR PRECEDENCE, which can be controlled
    with parentheses `()` for clarity and correctness.

HOW TO RUN THIS CODE:

1.  Save this file as `4_operators_and_comparisons.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 4_operators_and_comparisons.py`
'''