# -*- coding: utf-8 -*-
"""
Part 5, Lesson 26: Structuring a Multi-File Project (Utility Module)

Author: dunamismax
Date: 06-15-2025

This file is a "utility module." Its purpose is to contain a collection of
related, reusable functions that can be imported elsewhere in the project.
It is not meant to be run directly.
"""

# The lesson for this topic is in the README.md file.

def shout(text):
    """
    Converts a string to uppercase and adds an exclamation mark.
    
    Args:
        text (str): The string to process.
        
    Returns:
        str: The uppercased string with an exclamation mark.
    """
    # We assume text is a string. In a real application, you might add
    # error handling here (see Lesson 12).
    return text.upper() + "!"


def reverse(text):
    """
    Reverses a string using slicing.
    
    Args:
        text (str): The string to reverse.
        
    Returns:
        str: The reversed string.
    """
    # The [::-1] slice is a concise "Pythonic" way to reverse a sequence.
    return text[::-1]

# It's good practice to include this block in a module.
# If someone accidentally runs `python utils/string_helper.py`, this code
# will execute, informing them of the module's intended use.
if __name__ == "__main__":
    print("This is a utility module containing helper functions.")
    print("It is not meant to be run directly.")
    print("Please run 'main.py' instead.")