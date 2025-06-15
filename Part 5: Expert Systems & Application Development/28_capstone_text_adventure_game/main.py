# -*- coding: utf-8 -*-
"""
Part 5, Lesson 28: Capstone Project - Text Adventure Game (Main)

Author: dunamismax
Date: 06-15-2025

This is the main entry point for the Text Adventure Game.
Its only job is to create an instance of the GameEngine and run it.
"""

# The main lesson is in the README.md file. Read it first!

# We import the os module to help us build a reliable file path.
import os
from game.engine import GameEngine

# This is the standard way to make a script's location the reference point.
# __file__ is a special variable that holds the path to the current script.
# os.path.dirname() gets the directory part of that path.
# This gives us a reliable path to our project's root folder, no matter
# where the script is run from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# We now use os.path.join() to create a cross-platform, absolute path to
# our data file.
MAP_FILE_PATH = os.path.join(BASE_DIR, "game_data.json")

if __name__ == "__main__":
    
    print("Starting the Text Adventure Game...")
    
    # Create an instance of our game engine using the new, robust path.
    game = GameEngine(MAP_FILE_PATH)
    
    # Start the main game loop.
    game.run()
    
    # This message will be printed after the game loop has ended (i.e., when the
    # player quits the game).
    print("Thank you for playing!")