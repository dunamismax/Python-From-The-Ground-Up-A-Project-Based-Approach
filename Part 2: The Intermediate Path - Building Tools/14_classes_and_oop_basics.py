# -*- coding: utf-8 -*-
"""
Part 2, Lesson 14: Classes and OOP Basics

Author: dunamismax
Date: 06-15-2025

This lesson is a fundamental introduction to Object-Oriented Programming (OOP).
It covers the core concepts of classes, objects, the __init__ method,
attributes, and methods.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to one of the most important concepts in modern programming:
OBJECT-ORIENTED PROGRAMMING, or OOP. This is a big topic, but the core
idea is simple and incredibly powerful.

So far, we've worked with data types like strings, integers, lists, and
dictionaries. But what if we want to represent something more complex from the
real world, like a "User", a "Car", or a "Dog"? A dog isn't just a name (string)
or an age (integer); it's a single "thing" that HAS a name and an age, and it
can DO things, like bark or sit.

OOP allows us to create our own custom data types.

THE CORE IDEA: BLUEPRINTS AND OBJECTS
A CLASS is a BLUEPRINT for creating things. For example, we can create a `Dog`
class that defines what every dog should have (like a name and an age) and what
every dog should be able to do (like bark).

An OBJECT (also called an INSTANCE) is a specific thing created from that
blueprint. So, "Fido" could be one object created from the `Dog` class, and
"Lucy" could be another. They are both dogs, but they are separate objects with
their own specific data.

In this lesson, we will define a `Dog` class and then create dog objects from it.
'''

# --- Part 1: Defining a Class ---
# A class definition is the blueprint. It is standard practice to define
# classes at the top level of a module, outside the `if __name__ == "__main__"`
# block. The class name is conventionally written in PascalCase (each word
# capitalized, no underscores).

class Dog:
    """
    Represents a dog, with a name and an age.
    This is our blueprint.
    """
    
    # --- The `__init__` Method (The Constructor) ---
    # `__init__` is a special METHOD (a function inside a class) that is
    # automatically called whenever you create a new object from this class.
    # Its job is to "initialize" the object, setting up its starting data.
    # Methods that start and end with double underscores are special in Python.
    
    # WHAT IS `self`?
    # `self` is the most important and often most confusing part for beginners.
    # `self` refers to the specific INSTANCE of the object being created.
    # When you create a dog named Fido, `self` is Fido. When you create Lucy,
    # `self` is Lucy. It's how an object refers to itself.
    
    def __init__(self, name, age):
        # We are receiving the 'name' and 'age' that were passed in when
        # the object was created.
        
        print(f"A new dog named '{name}' is being created!")
        
        # We now store that data on the object itself. These stored variables
        # are called ATTRIBUTES.
        # `self.name = name` means "Set THIS specific dog's 'name' attribute
        # to the value of the 'name' variable we just received."
        self.name = name
        self.age = age

    # --- Defining Other Methods ---
    # Methods are functions that belong to a class. They define the BEHAVIORS
    # of an object. The first argument of any method is always `self`, which
    # gives the method access to the object's own attributes.
    
    def bark(self):
        """Makes the dog bark."""
        # This method can access the object's own name via `self.name`.
        return f"{self.name} says: Woof! Woof!"
        
    def get_human_years(self):
        """Calculates the dog's age in human years (a simple approximation)."""
        # This method uses the object's own age via `self.age`.
        return self.age * 7


# The main execution block starts here.
if __name__ == "__main__":
    
    # --- Part 2: Creating an Object (Instance) ---
    # Now that we have our `Dog` blueprint (the class), let's create some
    # actual dogs (the objects).
    #
    # To create an object, you call the class name like it's a function,
    # passing in the arguments required by the `__init__` method (excluding `self`).
    
    print("--- Part 2: Creating our first dog object ---")
    # This line calls `Dog.__init__(self, "Fido", 3)`. Python automatically
    # handles passing `self`.
    dog1 = Dog("Fido", 3)
    
    # `dog1` is now a `Dog` OBJECT. We can access its ATTRIBUTES using dot notation.
    print(f"Our first dog's name is: {dog1.name}")
    print(f"{dog1.name}'s age is: {dog1.age}")


    # --- Part 3: Using an Object's Methods ---
    # We can also call the methods we defined on our object.
    
    print("\n--- Part 3: Using the dog's methods ---")
    bark_sound = dog1.bark()
    print(bark_sound)
    
    human_age = dog1.get_human_years()
    print(f"In human years, {dog1.name} is {human_age} years old.")


    # --- Part 4: Creating Multiple, Independent Objects ---
    # The power of classes is creating many objects from the same blueprint.
    # Each object is independent and has its own data.
    
    print("\n--- Part 4: Creating a second dog object ---")
    dog2 = Dog("Lucy", 5)
    
    print(f"Our second dog's name is: {dog2.name}")
    print(f"Her age is: {dog2.age}")
    print(dog2.bark())
    
    # Notice that `dog1`'s data has not changed. It is a separate object.
    print(f"\nChecking our first dog again: {dog1.name}, age {dog1.age}.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Object-Oriented Programming is a way of thinking that helps you model the real
world in your code by bundling data and behavior together.

1.  A CLASS is a blueprint or template for creating objects.
2.  An OBJECT (or INSTANCE) is a specific item created from a class.
3.  ATTRIBUTES are variables that store the data belonging to an object (e.g.,
    `self.name`). They represent what the object *is*.
4.  METHODS are functions that belong to a class. They define what an object
    can *do* (e.g., `.bark()`).
5.  The `__init__` method is a special "constructor" method that runs when you
    create a new object, used to set up its initial attributes.
6.  The `self` keyword is how an object refers to itself, allowing methods to
    access that specific object's attributes and other methods.

This is a paradigm shift in programming. As we move forward, we'll see how
using classes allows us to build far more complex and organized applications.

HOW TO RUN THIS CODE:

1.  Save this file as `14_classes_and_oop_basics.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 14_classes_and_oop_basics.py`
'''