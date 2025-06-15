# -*- coding: utf-8 -*-
"""
Part 5, Lesson 26: Structuring a Multi-File Project (Main)

Author: dunamismax
Date: 06-15-2025

This file is the main entry point for the application. It demonstrates
how to import and use functions from other modules within a structured project.
"""

# The lesson for this topic is in the README.md file. Read it first!

'''
=====================================================================================
|                                   - PROJECT START -                                 |
=====================================================================================

This script demonstrates how a "main" file acts as the orchestrator.
It doesn't define the complex logic itself; instead, it imports the tools
it needs from other, specialized modules.
'''

# --- Part 1: Importing from a Custom Module ---
#
# This is the most important line in this file.
# 'from utils.string_helper' tells Python:
#   1. Look for a package (a folder with an __init__.py file) named 'utils'.
#   2. Inside that package, look for a file named 'string_helper.py'.
# 'import shout, reverse' tells Python:
#   3. Make the functions 'shout' and 'reverse' from that module available
#      for us to use in this file.
from utils.string_helper import shout, reverse

# This is the main execution block. In a multi-file project, it's absolutely
# critical. It ensures this code only runs when we execute `python main.py`,
# and not when another file imports something from `main.py`.
if __name__ == "__main__":
    
    print("--- Running the Main Application ---")

    # We have a list of phrases we want to process.
    phrases = ["hello world", "python is fun", "separation of concerns"]
    
    print(f"\nOriginal phrases: {phrases}")
    
    # --- Part 2: Using the Imported Functions ---
    # Now we can use `shout` and `reverse` as if they were defined right here.
    # This makes our main script clean and focused on the high-level goal,
    # not the low-level implementation details.
    
    print("\n--- Using the 'shout' helper function ---")
    for phrase in phrases:
        shouted_phrase = shout(phrase)
        print(shouted_phrase)
        
    print("\n--- Using the 'reverse' helper function ---")
    reversed_phrase = reverse("A man, a plan, a canal: Panama")
    print(f"Reversing 'A man, a plan, a canal: Panama' -> '{reversed_phrase}'")

    print("\nApplication finished.")

'''
=====================================================================================
|                                    - PROJECT END -                                  |
=====================================================================================

HOW TO RUN THIS PROJECT:

1. Open a terminal or command prompt.
2. Navigate to this directory: `26_structuring_a_multi_file_project/`.
3. Run the main script, NOT the helper files:
   `python main.py` 
   (or `python3 main.py` on some systems)

You should see the output from the `print` statements above, demonstrating
that `main.py` successfully imported and used the functions from the utils module.
'''