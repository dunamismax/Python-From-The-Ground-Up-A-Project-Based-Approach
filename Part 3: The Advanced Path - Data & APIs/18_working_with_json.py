# -*- coding: utf-8 -*-
"""
Part 3, Lesson 18: Working with JSON

Author: dunamismax
Date: 06-15-2025

This file introduces JSON (JavaScript Object Notation), the standard
format for data exchange on the web. It covers how to use Python's
built-in `json` module to parse JSON into Python objects and vice-versa.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

In our upcoming projects, we're going to communicate with the internet to get
live data from services called APIs (Application Programming Interfaces). When we
ask an API for data, it needs to send it back in a format that both humans and
computers can easily understand.

The most common format for this is JSON (JavaScript Object Notation).

WHAT IS JSON?
JSON is a lightweight, text-based data format. Its syntax is very similar to
how we define Python dictionaries and lists. This makes it incredibly easy to
work with in Python.

A Python dictionary: `{"name": "Alice", "age": 30, "is_student": False}`
The same data in JSON: `{"name": "Alice", "age": 30, "is_student": false}`

Notice the small differences: Python's `False` is `false` in JSON. Similarly,
Python's `True` becomes `true` and `None` becomes `null`.

Python has a built-in module called `json` that makes converting between these
formats trivial. The process of converting a Python object (like a dictionary
or list) into a JSON string is called SERIALIZATION or ENCODING. The reverse,
converting a JSON string into a Python object, is called DESERIALIZATION or
DECODING.
'''

# We must first import the `json` module to use its functions.
import json

# The main execution block starts here.
if __name__ == "__main__":

    # Let's start with a sample Python dictionary. This is our "Python object".
    user_profile = {
        "username": "coder_jane",
        "email": "jane@example.com",
        "posts_authored": 15,
        "is_active": True,
        "followed_tags": ["python", "datascience", "webdev"],
        "last_login": None
    }

    print("--- Our original Python dictionary ---")
    print(user_profile)
    print(f"Type of our data: {type(user_profile)}")
    

    # --- Part 1: SERIALIZATION - Python Object to JSON String ---
    # To convert a Python object into a JSON formatted string, we use the
    # `json.dumps()` function. The 's' stands for 'string'.

    print("\n--- Part 1: Python object to JSON string (Serialization) ---")
    
    # The `indent=4` argument is optional but highly recommended. It makes
    # the resulting JSON string human-readable by pretty-printing it.
    json_string = json.dumps(user_profile, indent=4)
    
    print("The data converted to a JSON string:")
    print(json_string)
    print(f"Type of the result: {type(json_string)}")
    
    # Notice the changes: `True` became `true`, and `None` became `null`.
    # The output is now a single, multi-line STRING.


    # --- Part 2: DESERIALIZATION - JSON String to Python Object ---
    # Now, let's do the reverse. To convert a JSON string back into a Python
    # object, we use the `json.loads()` function. Again, 's' for 'string'.

    print("\n--- Part 2: JSON string to Python object (Deserialization) ---")
    
    # `json.loads()` takes a string as input and parses it.
    python_object = json.loads(json_string)
    
    print("The JSON string converted back into a Python object:")
    print(python_object)
    print(f"Type of the result: {type(python_object)}")
    
    # We can now access it like a normal dictionary again.
    print(f"Username from the parsed object: {python_object['username']}")


    # --- Part 3: Writing JSON to a File ---
    # A very common task is to save our data to a file in JSON format.
    # For this, we use `json.dump()` (without the 's'). This function writes
    # the object directly to a file-like object.
    
    print("\n--- Part 3: Writing JSON to a file ---")
    
    # We use `with open(...)` which you learned in Lesson 10.
    # The first argument is the Python object, the second is the file handler.
    file_path = "user_profile.json"
    with open(file_path, 'w') as json_file:
        json.dump(user_profile, json_file, indent=4)
        
    print(f"Data has been successfully written to the file '{file_path}'.")
    print("Go check for this new file in your directory!")


    # --- Part 4: Reading JSON from a File ---
    # Finally, let's read the data back from the file we just created.
    # For this, we use `json.load()` (again, no 's'). It reads from a
    # file-like object and deserializes its content.
    
    print("\n--- Part 4: Reading JSON from a file ---")
    
    try:
        with open(file_path, 'r') as json_file:
            loaded_data = json.load(json_file)
        
        print(f"Data successfully loaded from '{file_path}':")
        print(loaded_data)
        print(f"Type of loaded data: {type(loaded_data)}")
        print(f"Loaded user's email: {loaded_data['email']}")
        
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just learned how to work with JSON, the universal language of data
exchange on the internet. This skill is essential for almost any application
that interacts with web services.

1.  JSON (JavaScript Object Notation) is a text-based format that looks very
    similar to Python dictionaries and lists.

2.  The built-in `json` module is your tool for working with JSON data.

3.  SERIALIZATION (Python -> JSON):
    - `json.dumps(obj)`: Converts a Python object to a JSON formatted STRING.
    - `json.dump(obj, file)`: Writes a Python object to a FILE in JSON format.

4.  DESERIALIZATION (JSON -> Python):
    - `json.loads(str)`: Parses a JSON formatted STRING into a Python object.
    - `json.load(file)`: Reads from a FILE and parses its JSON content into a
      Python object.

Remember the 's': if it has an 's' (`dumps`/`loads`), it works with strings.
If it doesn't (`dump`/`load`), it works with files.

In the next lesson, we will use this knowledge to build an app that fetches
live data from a real-world API!

HOW TO RUN THIS CODE:

1.  Save this file as `18_working_with_json.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 18_working_with_json.py`
5.  After running, a new file named `user_profile.json` should appear.
'''