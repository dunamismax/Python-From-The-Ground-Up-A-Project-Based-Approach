# -*- coding: utf-8 -*-
"""
Part 4, Lesson 21: Virtual Environments and Requirements

Author: dunamismax
Date: 06-15-2025

This file explains the professional practice of using virtual environments
to manage project dependencies and how to use requirements files to
share and replicate these environments.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to the Expert Path! So far, we've used `pip` to install packages like
`requests` for our API project. When you run `pip install <package>`, it typically
installs the package globally, meaning it's available to every Python script
on your system.

This seems convenient, but it leads to a major problem in real-world development:
- Project A might need `requests version 2.25`.
- A new Project B might need `requests version 2.28`.
If you upgrade `requests` for Project B, you might accidentally break Project A!
This is often called "dependency hell".

The solution is a core tool for all modern Python developers:
The VIRTUAL ENVIRONMENT.

A VIRTUAL ENVIRONMENT is an isolated, self-contained directory that holds a
specific Python interpreter and all the specific packages a single project needs.
Think of it like giving each project its own private, clean workshop, instead
of having all your tools jumbled in one giant, shared garage.

This lesson is different from others. The primary "code" you'll be writing is not
in a Python script, but in your TERMINAL or COMMAND PROMPT. This file will serve
as your guide.
'''

# --- Part 1: Creating a Virtual Environment with `venv` ---
#
# Python comes with a built-in module called `venv` for creating virtual
# environments. The process is simple.
#
# First, you navigate to your main project folder in your terminal. For example,
# you might create a new folder called `my_new_project`.
#
#   `cd path/to/my_new_project`
#
# Then, you run the following command:
#
#   `python -m venv venv`
#
# Let's break that command down:
# - `python -m venv`: This tells Python to run the `venv` module as a script.
# - `venv`: The second `venv` is the NAME we are giving to the folder that will
#   contain our virtual environment. `venv` is the standard, conventional name,
#   and you should stick to it.
#
# After running this, you'll see a new folder named `venv` inside your project
# directory. This folder contains a copy of the Python interpreter and is ready
# to hold all of your project's private packages.


# --- Part 2: Activating and Deactivating the Environment ---
#
# Just creating the environment isn't enough. You have to "enter" or ACTIVATE it.
# This tells your terminal session to use the Python and pip located inside the
# `venv` folder instead of the global ones.
#
# The command differs slightly based on your operating system.
#
# On macOS and Linux:
#   `source venv/bin/activate`
#
# On Windows (Command Prompt or PowerShell):
#   `.\venv\Scripts\activate`
#
# When activated, you will usually see your command prompt change to show the
# environment's name, like `(venv) C:\path\to\my_project>`. This is how you know
# you are inside your isolated environment.
#
# To exit the environment, simply type:
#   `deactivate`
#
# Your prompt will return to normal, and you'll be back to using your system's
# global Python installation.


# --- Part 3: Managing Dependencies with `requirements.txt` ---
#
# Now that you have an isolated environment, how do you share your project with
# someone else, ensuring they use the exact same package versions you did?
#
# The standard way is with a REQUIREMENTS FILE, almost always named `requirements.txt`.
#
# STEP 1: Generate the file.
# While your virtual environment is ACTIVE, install a package. Let's use `requests`
# as an example, which we'll need for our next project.
#
#   `(venv) $ pip install requests`
#
# Now, to save a list of all packages installed in this environment, run:
#
#   `(venv) $ pip freeze > requirements.txt`
#
# - `pip freeze`: This command lists all the packages and their exact versions.
# - `>`: This is a standard shell operator that REDIRECTS the output of a command
#   into a file instead of printing it to the screen.
#
# This creates a `requirements.txt` file in your project folder. It will look
# something like this (versions may vary):
#   certifi==2023.7.22
#   charset-normalizer==3.3.2
#   idna==3.6
#   requests==2.31.0
#   urllib3==2.1.0
#
# STEP 2: Install from the file.
# Now, another developer can clone your project, create their own virtual
# environment, activate it, and run one simple command to install everything:
#
#   `(venv) $ pip install -r requirements.txt`
#
# This command tells `pip` to read the file and install all the listed packages,
# creating a perfect replica of your development environment.


# This `if` block is the main entry point of our script.
# For this lesson, we'll just print a summary of the workflow.
if __name__ == "__main__":
    print("--- Professional Python Project Workflow ---")
    print("\nThis Python file is a guide. The real work is done in your terminal.")
    print("Here is the standard workflow for starting a new project:")

    workflow = [
        "1. Create a new project folder and navigate into it.",
        "   `mkdir my_new_project && cd my_new_project`",
        "2. Create a virtual environment.",
        "   `python -m venv venv`",
        "3. Activate the virtual environment.",
        "   (macOS/Linux): `source venv/bin/activate`",
        "   (Windows): `.\\venv\\Scripts\\activate`",
        "4. Install your project's packages.",
        "   `pip install <package1> <package2> ...`",
        "5. Develop your Python code (e.g., in `main.py`).",
        "6. Save your project's dependencies to a file.",
        "   `pip freeze > requirements.txt`",
        "7. When you are finished working, deactivate the environment.",
        "   `deactivate`"
    ]

    for step in workflow:
        print(step)

    print("\nFrom now on, all our projects will use this professional workflow!")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just learned one of the most important professional practices in Python
development. This skill separates hobbyists from professional developers.

1.  A VIRTUAL ENVIRONMENT (`venv`) isolates your project's dependencies from
    your system and other projects, preventing version conflicts.
2.  You create it with `python -m venv venv` and activate it to start working.
3.  A `requirements.txt` file is the standard way to define and share your
    project's exact package dependencies.
4.  You create it with `pip freeze > requirements.txt`.
5.  You install from it with `pip install -r requirements.txt`.

This workflow ensures that your projects are portable, reproducible, and robust.
We will use this for every multi-package project going forward.

HOW TO "RUN" THIS LESSON:

1.  Read this file from top to bottom.
2.  Open your terminal or command prompt.
3.  Create a practice project folder (e.g., `mkdir test_env && cd test_env`).
4.  Follow the commands outlined in the comments above to create, activate,
    install a package, freeze requirements, and deactivate the environment.
5.  Running this Python file (`python 21_...py`) will only print a summary of
    the workflow; the real learning comes from doing it yourself in the terminal.
'''