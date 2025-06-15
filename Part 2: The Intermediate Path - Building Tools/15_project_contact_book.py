# -*- coding: utf-8 -*-
"""
Part 2, Lesson 15: Project: Contact Book

Author: dunamismax
Date: 06-15-2025

This file is a capstone project for Part 2. It builds a complete
command-line contact book application, utilizing classes for data modeling,
file I/O for data persistence, and functions for organized logic.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

PROJECT BRIEF: A PERSISTENT CONTACT BOOK

Welcome to your second major project! We are going to build a fully functional
contact book that runs in the terminal. This project is designed to bring
together everything you have learned in Part 2.

Our application will be able to:
1.  Add a new contact (name, phone, email).
2.  View all saved contacts.
3.  Search for a specific contact by name.
4.  Delete a contact.
5.  Save all contacts to a file, so the data PERSISTS between uses.
6.  Automatically load contacts from the file when the program starts.

KEY CONCEPTS WE WILL USE:
-   CLASSES & OOP: We will create a `Contact` class to be the blueprint for
    every contact we create. This is the perfect use case for OOP, as it
    bundles the contact's data (attributes) and behaviors (methods) together.
-   FILE I/O: We'll use `with open(...)` to read from and write to a `.txt`
    file, which will act as our simple database.
-   LISTS & DICTIONARIES: A list will be our primary way to hold all the
    `Contact` objects while the program is running.
-   FUNCTIONS: We'll break down every feature (add, view, save, load) into its
    own function to keep our code clean, organized, and easy to read.
-   MODULES: The `os` module will be used to check if our save file exists.
-   EXCEPTION HANDLING: We'll use `try...except` to prevent crashes when the
    user enters invalid data (e.g., a non-numeric choice).

This is a significant step up in complexity, but it mirrors how real-world
applications are built.
'''

import os

# --- The Blueprint: Our Contact Class ---
# We define the class at the top level so it's available to our whole script.
class Contact:
    """
    Represents a single contact with a name, phone number, and email.
    """
    def __init__(self, name, phone, email):
        """Initializes a Contact object with its attributes."""
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        A special method that returns a user-friendly string representation
        of the object. This is automatically called when you try to `print()`
        an object of this class. It's incredibly useful!
        """
        return f"Name: {self.name:<20} | Phone: {self.phone:<15} | Email: {self.email}"

    def to_csv_line(self):
        """
        Returns a string formatted for saving to a file, with values
        separated by commas. This is a simple version of the CSV format.
        """
        return f"{self.name},{self.phone},{self.email}\n"


# --- Application Logic Functions ---

def load_contacts(filename):
    """Loads contacts from a file and returns them as a list of Contact objects."""
    contacts = []
    if not os.path.exists(filename):
        # If the file doesn't exist yet, just return an empty list.
        return contacts
    
    with open(filename, "r") as f:
        for line in f:
            # We strip whitespace and split the line by the comma delimiter.
            parts = line.strip().split(',')
            if len(parts) == 3: # Ensure the line is not malformed
                # Create a new Contact object and add it to our list.
                contacts.append(Contact(parts[0], parts[1], parts[2]))
    print(f"Loaded {len(contacts)} contacts from {filename}.")
    return contacts

def save_contacts(filename, contacts):
    """Saves the list of Contact objects to a file."""
    with open(filename, "w") as f:
        for contact in contacts:
            f.write(contact.to_csv_line())
    print(f"Saved {len(contacts)} contacts to {filename}.")

def print_menu():
    """Prints the main menu options to the console."""
    print("\n--- Python Contact Book ---")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search for Contact")
    print("4. Delete Contact")
    print("5. Save and Exit")
    print("---------------------------")

def add_contact(contacts_list):
    """Prompts user for details and adds a new contact to the list."""
    print("\n-- Add New Contact --")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts_list.append(Contact(name, phone, email))
    print("Contact added successfully!")

def view_contacts(contacts_list):
    """Displays all contacts in a formatted way."""
    print("\n-- All Contacts --")
    if not contacts_list:
        print("Your contact book is empty.")
        return
        
    # We use enumerate to get both the index (for numbering) and the item.
    for i, contact in enumerate(contacts_list):
        # The `__str__` method of our Contact class does the heavy lifting here!
        print(f"{i + 1}: {contact}")

def search_contacts(contacts_list):
    """Searches for contacts by name."""
    print("\n-- Search Contacts --")
    search_term = input("Enter the name to search for: ").lower().strip()
    found_contacts = []
    for contact in contacts_list:
        if search_term in contact.name.lower():
            found_contacts.append(contact)
            
    if not found_contacts:
        print(f"No contacts found matching '{search_term}'.")
    else:
        print("Found the following contacts:")
        for contact in found_contacts:
            print(f"- {contact}")

def delete_contact(contacts_list):
    """Deletes a contact by its number in the list."""
    print("\n-- Delete Contact --")
    view_contacts(contacts_list)
    if not contacts_list:
        return
        
    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(contacts_list):
            # We subtract 1 because lists are 0-indexed.
            removed_contact = contacts_list.pop(choice - 1)
            print(f"Successfully deleted: {removed_contact.name}")
        else:
            print("Invalid number. Please choose a number from the list.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# --- Main Application Execution ---
if __name__ == "__main__":
    
    FILENAME = "contacts.txt"
    contacts = load_contacts(FILENAME)
    
    # This is the main loop of our application.
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            save_contacts(FILENAME, contacts)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations! You have successfully built a complete, persistent application.
This project demonstrates the power of combining classes, file handling, and
structured functions to create something truly useful.

By modeling our data with a `Contact` class, the rest of our code became much
cleaner. Instead of passing around separate lists of names, phones, and emails,
we passed around a single list of `Contact` objects. This is the essence of
what makes Object-Oriented Programming so powerful for organizing complex data.

You have now completed Part 2 and have a strong intermediate foundation. In Part 3,
we'll explore more advanced data structures and venture into the exciting world
of APIs and working with data from the internet.

HOW TO RUN THIS CODE:

1.  Save this file as `15_project_contact_book.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 15_project_contact_book.py`
5.  Interact with the menu. Add some contacts, view them, and then choose
    "Save and Exit". A `contacts.txt` file will be created.
6.  Run the program again. You will see your contacts are automatically loaded!
'''