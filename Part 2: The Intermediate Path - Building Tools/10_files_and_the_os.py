# -*- coding: utf-8 -*-
"""
Part 2, Lesson 10: Files and the OS

Author: dunamismax
Date: 06-15-2025

This file serves as the lesson and demonstration for interacting with files
and the operating system. It covers creating, writing to, appending to,
and reading from files, as well as using the 'os' module to check for a
file's existence and to delete it.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to Part 2! You've mastered the basics of Python's data structures
and logic. Now, we'll start building more powerful and practical tools.

So far, all the data our programs have used (variables, lists, dictionaries)
has been stored in the computer's memory (RAM). When the program finishes,
that memory is wiped clean and all our data is lost.

To save data permanently, we need to store it in a FILE on the hard drive.
This concept is called PERSISTENCE.

In this lesson, we will learn how to:
1.  Write data to a text file.
2.  Read data from a text file.
3.  Use the built-in `os` module to interact with the file system itself.
'''

# We will use Python's built-in `os` module later in this lesson.
# A MODULE is a file containing Python code and definitions. To use a module,
# you must first IMPORT it, which makes its functions available to your script.
# It is standard practice to place imports at the top of a file.
import os


# The main execution block starts here.
if __name__ == "__main__":

    # Let's define the name of the file we'll be working with.
    # Using a variable for the filename is good practice, as it makes it
    # easy to change if you need to.
    notes_filename = "my_notes.txt"


    # --- Part 1: Writing to a File with 'w' Mode ---
    # To work with a file, we use the built-in `open()` function.
    # The safest way to do this is with a `with` statement. This is called a
    # CONTEXT MANAGER. It automatically handles opening and, more importantly,
    # safely CLOSING the file for you, even if errors occur.
    #
    # `open()` takes two main arguments: the filename and the MODE.
    # MODE 'w' stands for WRITE.
    #
    # CAUTION: Using 'w' mode will CREATE the file if it doesn't exist, but it
    # will COMPLETELY OVERWRITE and erase the file if it already exists.

    print("--- Part 1: Writing to a File ---")

    # The syntax is `with open(filename, mode) as file_variable:`
    with open(notes_filename, "w") as f:
        # `f` is now a variable representing our open file.
        # We use the `.write()` method to write a string to it.
        f.write("Hello, files!\n")
        f.write("This is my first line of permanent data.\n")
        # Note: `.write()` does not automatically add a new line. We must add
        # the newline character `\n` ourselves if we want one.
        f.write("This is the third and final line for now.")

    print(f"Successfully wrote initial content to '{notes_filename}'")
    print("Go check your file system! The file should be there.")


    # --- Part 2: Appending to a File with 'a' Mode ---
    # Overwriting a file every time is often not what we want. To add new
    # content to the end of an existing file, we use MODE 'a' for APPEND.
    # If the file doesn't exist, 'a' mode will create it.

    print("\n--- Part 2: Appending to a File ---")
    
    with open(notes_filename, "a") as f:
        # This new content will be added to the end of the file.
        f.write("\n\nThis new line was appended later.")

    print(f"Successfully appended content to '{notes_filename}'")


    # --- Part 3: Reading from a File with 'r' Mode ---
    # To get data out of a file, we open it in MODE 'r' for READ.
    # This is the most common operation and is the default mode if you don't
    # specify one.

    print("\n--- Part 3: Reading from a File ---")

    with open(notes_filename, "r") as f:
        # The `.read()` method reads the ENTIRE contents of the file into a
        # single string. This is simple but can use a lot of memory for large files.
        full_content = f.read()
    
    print("Contents of the file read all at once:")
    print("---------------------------------------")
    print(full_content)
    print("---------------------------------------")

    # A better and more "Pythonic" way to read a file is to loop through it
    # line by line. This is much more memory-efficient.
    print("\nReading the file line by line:")
    with open(notes_filename, "r") as f:
        for line in f:
            # The `line` variable includes the invisible newline character `\n`
            # at the end. We can use `.strip()` (from Lesson 3) to remove it!
            print(f"  - {line.strip()}")


    # --- Part 4: Using the `os` Module to Manage Files ---
    # What if we want to delete our file after we're done? Or check if a file
    # exists before we try to read it (to prevent an error)?
    # The `os` module provides functions to interact with the OPERATING SYSTEM.

    print("\n--- Part 4: Using the `os` module ---")

    # `os.path.exists()` checks if a file or directory exists. It returns a
    # boolean: True or False. This is extremely useful for error prevention.
    print(f"Checking if '{notes_filename}' exists...")
    if os.path.exists(notes_filename):
        print("  - Yes, the file exists.")
        
        # `os.remove()` deletes a file.
        # CAUTION: This is a permanent action. The file is gone for good!
        print(f"  - Deleting '{notes_filename}'...")
        os.remove(notes_filename)
        print("  - File deleted.")
    else:
        print("  - No, the file does not exist.")

    # Let's check again to confirm it's gone.
    print(f"Checking again if '{notes_filename}' exists...")
    if not os.path.exists(notes_filename):
        print("  - Confirmed, the file is now gone.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just gained a superpower: PERSISTENCE! Your programs can now save
data that lasts even after they've finished running.

1.  The `with open(filename, mode) as f:` structure is the standard, safe way
    to work with files in Python. It handles closing the file automatically.
2.  The three primary file MODES are:
    - 'w' (WRITE): Creates a new file or overwrites an existing one.
    - 'a' (APPEND): Adds content to the end of a file, creating it if needed.
    - 'r' (READ): Retrieves content from a file.
3.  You can read a file all at once with `.read()` or, more efficiently, line
    by line using a `for` loop.
4.  The `os` MODULE allows your program to interact with the file system. We
    used `os.path.exists()` to check if a file exists and `os.remove()` to
    delete it permanently.

HOW TO RUN THIS CODE:

1.  Save this file as `10_files_and_the_os.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 10_files_and_the_os.py`

OBSERVE: As the script runs, you will see a file named `my_notes.txt` appear in
the same folder. Then, by the time the script finishes, it will be gone because
the script cleaned up after itself by deleting it.
'''