# -*- coding: utf-8 -*-
"""
Part 5, Lesson 29: Packaging Your Project with pyproject.toml

Author: dunamismax
Date: 06-15-2025

This file is a conceptual lesson explaining the modern Python packaging
workflow. It describes how to prepare a project to be shared and installed
by others using `pip`.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

So you've built an amazing project like our Text Adventure Game. How do you
share it so that a friend can just type `pip install your-game` and run it?
The answer is PACKAGING.

Packaging is the process of bundling your Python code, metadata (like the
project name, version, and author), and dependencies into a standard format
that can be distributed and installed easily.

In the past, this was done with a file called `setup.py`. The modern, standard
way is to use a single configuration file: `PYPROJECT.TOML`.

WHAT IS TOML?
TOML (Tom's Obvious, Minimal Language) is a simple configuration file format.
It's designed to be easy for humans to read. We use it to tell Python's
build tools everything they need to know about our project.

This lesson will walk you through the concepts and files needed to package
a simple command-line tool. Since this involves multiple files and folders,
we will *simulate* their contents using print statements.
'''

# We place our code inside the main execution block.
# This file is for learning; there is no complex program to run here.
if __name__ == "__main__":

    # --- Part 1: The Project Structure for Packaging ---
    #
    # To package a project, we need a specific folder structure. The most common
    # modern layout is the "src" layout. It clearly separates your actual
    # source code from other project files like READMEs and config files.
    
    print("--- Part 1: A Standard Project Structure ---")
    
    project_structure = """
    my_greeter_tool/
    ├── pyproject.toml      <-- The most important file for packaging!
    ├── README.md           <-- Your project's description.
    ├── LICENSE             <-- The license file (e.g., MIT).
    └── src/                <-- A directory for your source code.
        └── greeter/        <-- This is the actual Python package.
            ├── __init__.py <-- Makes 'greeter' a package.
            └── cli.py      <-- Our script's logic and entry point function.
    """
    print("A recommended project layout:")
    print(project_structure)
    
    
    # --- Part 2: The Python Code with an Entry Point ---
    #
    # Your script needs a clear entry point function. This is the function
    # that will be run when the user types your command in their terminal.
    # We will put this logic inside `src/greeter/cli.py`.
    
    print("\n--- Part 2: The Code (`src/greeter/cli.py`) ---")
    
    cli_py_content = """
    # src/greeter/cli.py

    def main():
        \"\"\"The main entry point function for our script.\"\"\"
        print("Hello! Welcome to your first packaged Python application!")
        print("This message is coming from the 'greeter' tool.")

    # Note: No `if __name__ == "__main__":` is needed here, because this
    # function is intended to be called by the packaging tools, not by
    # running the file directly.
    """
    print("Contents of the script file:")
    print(cli_py_content)
    
    
    # --- Part 3: The `pyproject.toml` Configuration File ---
    #
    # This is the heart of the packaging process. It contains all the metadata
    # and build instructions. Let's look at a well-commented example.
    
    print("\n--- Part 3: The `pyproject.toml` file ---")
    
    pyproject_toml_content = r'''
# pyproject.toml

# This first section tells build tools what they need to build your project.
# For most projects using the `setuptools` backend, this is boilerplate.
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

# This is the main section where you define your project's metadata.
# This information is what will appear on PyPI (the Python Package Index).
[project]
name = "my-greeter-tool"
version = "0.1.0"
authors = [
  { name="dunamismax", email="author@example.com" },
]
description = "A simple example package that greets the user."
readme = "README.md"  # Path to your README file.
requires-python = ">=3.8"
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
# If your project depends on other packages (like `requests`), you list them here.
# dependencies = [
#   "requests",
# ]

# This section creates the command-line script.
[project.scripts]
# This line means:
# "Create a command named 'greet' that runs the 'main' function
#  found in the 'greeter.cli' module."
greet = "greeter.cli:main"
'''
    print("Contents of `pyproject.toml`:")
    print(pyproject_toml_content)
    
    
    # --- Part 4: The Build Process ---
    #
    # Once your files are in place, you use standard tools to build the package.
    
    print("\n--- Part 4: The Build Process (Commands) ---")
    
    build_steps = """
# Step 1: Install the necessary build tools (you only do this once).
> pip install build twine

# Step 2: Run the build command from the root of your project directory
#         (the one containing `pyproject.toml`).
> python -m build

# After running this, a new 'dist/' directory will be created. It contains:
#   - my_greeter_tool-0.1.0-py3-none-any.whl  <-- The WHEEL file. A modern, fast-installing format.
#   - my_greeter_tool-0.1.0.tar.gz           <-- The SDIST (Source Distribution). A fallback.

# Step 3 (Optional): Upload your package to the Python Package Index (PyPI).
# This makes it publicly available for anyone to `pip install`.
# (You would first need to create an account on pypi.org).
> twine upload dist/*
"""
    print("The commands to build and distribute your package:")
    print(build_steps)
    
    print("\nAfter a successful `pip install .` or `pip install my-greeter-tool`,")
    print("the user can simply type `greet` in their terminal:")
    print("\n> greet")
    print("Hello! Welcome to your first packaged Python application!")
    print("This message is coming from the 'greeter' tool.\n")


'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just learned the fundamentals of modern Python packaging! This is a
critical skill for sharing your work and contributing to the open-source community.

1.  **Project Structure:** Use a `src` layout to keep your source code neatly
    organized and separate from configuration files.
2.  **`pyproject.toml`:** This is the single, standard configuration file for
    defining your project's name, version, author, dependencies, and entry points.
3.  **Entry Point:** Create a main function in your code (e.g., `main()`) that
    will be executed when a user runs your installed command.
4.  **`[project.scripts]`:** This special section in `pyproject.toml` links a
    terminal command (e.g., `greet`) to your entry point function.
5.  **The Workflow:** The process is standardized:
    *   Install tools: `pip install build twine`.
    *   Build packages: `python -m build`.
    *   Upload (optional): `twine upload dist/*`.

While there's more to learn (like including data files or handling complex
dependencies), you now understand the core concepts behind making your Python
projects installable and shareable with the world.

HOW TO RUN THIS CODE:

This file is a conceptual lesson and is meant to be read, not executed to
perform a task. Running it will simply print the contents of the example files
and the build commands to your console, guiding you through the process.

`python 29_packaging_your_project_with_pyproject.py`
'''