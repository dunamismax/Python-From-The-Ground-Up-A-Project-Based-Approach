# -*- coding: utf-8 -*-
"""
Part 5, Lesson 27: Introduction to GUIs with Tkinter

Author: dunamismax
Date: 06-15-2025

This file provides a first look at creating Graphical User Interfaces (GUIs)
with Python's built-in Tkinter library. It moves beyond console applications
to create interactive windows with buttons, labels, and input fields.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to the world of visual applications! Until now, all our programs have
run in the text-based console (the terminal). We've used `print()` to show
output and `input()` to get user data.

Now, we'll learn to create a GRAPHICAL USER INTERFACE (GUI) - a program with
windows, buttons, text boxes, and other visual elements that users can interact
with using their mouse and keyboard.

For this, we will use TKINTER (pronounced "tee-kay-inter"), which is the standard,
built-in GUI toolkit for Python. It's not the most modern-looking library, but it
is included with every Python installation, making it the perfect place to start.

Core Concepts of a GUI Application:
1.  THE ROOT WINDOW: This is the main window of your application that contains
    all other elements.
2.  WIDGETS: These are the building blocks of a GUI, such as buttons, labels,
    text entry fields, etc.
3.  GEOMETRY MANAGEMENT: This is how you control the placement and layout of
    widgets within the window (e.g., stacking them, arranging them in a grid).
4.  THE EVENT LOOP: This is a continuous loop that runs in the background,
    listening for user actions like mouse clicks or key presses (these are
    called EVENTS). When an event occurs, the loop can trigger a function
    in response.
'''

# We import the tkinter library. It's common practice to alias it as `tk`.
import tkinter as tk
# We also import `ttk`, which contains "themed widgets". They generally look
# a bit more modern than the classic tk widgets.
from tkinter import ttk

# --- Part 1: Structuring a GUI App with a Class ---
#
# While you can create a simple GUI with just functions, it's a very common
# and effective practice to organize your GUI code inside a CLASS.
# This keeps all the related widgets and functions neatly bundled together.
# This approach builds directly on what we learned in Lesson 14 about OOP.

class GreeterApp:
    """
    A simple GUI application that greets the user.
    This class encapsulates all the widgets and logic for our app.
    """

    # The __init__ method is perfect for setting up our GUI.
    # The `master` argument is the parent window that this class will control.
    def __init__(self, master):
        # We store the master window (the root) as an attribute so we can
        # refer to it later.
        self.master = master
        master.title("Greeter Application")
        # Let's give the window a minimum size so it doesn't look too cramped.
        master.minsize(300, 150)

        # We will now create all the WIDGETS and add them to our window.

        # --- Part 2: Creating Widgets and a Layout Frame ---
        #
        # To better organize our widgets, we can place them inside a Frame.
        # A Frame is an invisible container widget.
        # We use `ttk` for a modern look.
        self.frame = ttk.Frame(master, padding="20")
        
        # GEOMETRY MANAGEMENT: The `.pack()` method is one of Tkinter's
        # "geometry managers". It's the simplest one: it just stacks widgets
        # on top of each other or side-by-side.
        # `expand=True` and `fill='both'` make the frame grow if the user
        # resizes the window.
        self.frame.pack(expand=True, fill='both')

        # Create a LABEL widget. A label is used to display static text.
        # The first argument is always the parent widget it belongs to (our frame).
        self.name_label = ttk.Label(self.frame, text="Enter your name:")
        self.name_label.pack() # Stack it at the top of the frame.

        # Create an ENTRY widget. This is a single-line text box for user input.
        # We will use a `tk.StringVar` to easily get and set the text in this box.
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self.frame, textvariable=self.name_var)
        self.name_entry.pack() # Stack it below the label.

        # Create a BUTTON widget. When clicked, it will perform an action.
        # The `command` option is crucial: it specifies the function (or method)
        # to call when the button is pressed. This is our EVENT HANDLER.
        self.greet_button = ttk.Button(self.frame, text="Greet Me!", command=self.greet)
        self.greet_button.pack(pady=10) # `pady` adds some vertical padding.

        # Create another Label to display our greeting. We start it with empty text.
        self.greeting_label = ttk.Label(self.frame, text="")
        self.greeting_label.pack()

    # --- Part 3: The Event Handler Method ---
    #
    # This is the method that the `greet_button` will call when it's clicked.
    # A function that is called in response to an event is often called a
    # CALLBACK function.
    def greet(self):
        """Called when the greet_button is pressed."""
        # `.get()` is how we retrieve the current text from our Entry widget's
        # associated StringVar.
        name = self.name_var.get()
        
        # If the user didn't type anything, use a default name.
        if not name:
            name = "World"
        
        greeting_message = f"Hello, {name}!"
        
        # `.config()` is used to change the properties of a widget after it has
        # been created. Here, we change the `text` of our greeting_label.
        self.greeting_label.config(text=greeting_message)


# --- The Main Execution Block ---
# This is where we create the main window and start the application.
if __name__ == "__main__":
    
    # 1. Create the ROOT WINDOW. This is the main top-level window.
    #    It's a convention to name it `root`.
    root = tk.Tk()

    # 2. Instantiate our application class. We pass the `root` window
    #    to our class's __init__ method, making it the `master`.
    app = GreeterApp(root)

    # 3. Start the EVENT LOOP.
    #    The `root.mainloop()` call is essential. It tells Tkinter to show the
    #    window and listen for events (like button clicks or window closing).
    #    Your script will pause here, running the GUI, and will only continue
    #    past this line when the window is closed.
    print("Starting the Tkinter event loop...")
    root.mainloop()
    print("Tkinter event loop has finished. Program is exiting.")


'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

You've just built your first graphical application! This is a huge leap from
command-line programs.

1.  A GUI is built from a main ROOT WINDOW (`tk.Tk()`) and a collection of
    WIDGETS (Labels, Buttons, Entries).
2.  It's excellent practice to organize your GUI code within a CLASS to keep
    it structured and maintainable.
3.  GEOMETRY MANAGERS like `.pack()` are used to position widgets inside their
    parent container.
4.  The `command` option of a Button links it to a CALLBACK function (an event
    handler) that runs when the button is clicked.
5.  The entire application is driven by an EVENT LOOP (`root.mainloop()`), which
    waits for user input and dispatches events to their handlers.

Tkinter is a deep library with many more widgets and features, but you now
understand the fundamental principles behind all GUI programming.

HOW TO RUN THIS CODE:

1.  Save this file as `27_intro_to_gui_with_tkinter.py`.
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved this file.
4.  Run the file with the command: `python 27_intro_to_gui_with_tkinter.py`

Instead of seeing text in your terminal, a new window should appear on your
screen! Type your name in the box and click the button to see it in action.
Close the window to end the program.
'''