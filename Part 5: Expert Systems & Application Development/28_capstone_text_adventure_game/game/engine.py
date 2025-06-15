# -*- coding: utf-8 -*-
"""
Part 5, Lesson 28: Game Engine Module

Author: dunamismax
Date: 06-15-2025

This module defines the GameEngine, the main class that drives the game.
It contains the game loop, command parser, and coordinates the player and world.
"""

from .player import Player
from .world import World

class GameEngine:
    """
    The main engine for the text adventure game.
    """
    def __init__(self, map_file):
        """
        Initializes the GameEngine.

        Args:
            map_file (str): The path to the world data file.
        """
        self.world = World(map_file)
        self.player = Player(self.world.start_room_id)
        self.is_running = True

    def run(self):
        """Starts and runs the main game loop."""
        self.show_intro()
        
        while self.is_running:
            # We safely get the current room ONCE at the start of the loop.
            current_room = self.world.get_room(self.player.current_location_id)
            
            # This check now protects all subsequent code in this loop iteration.
            if not current_room:
                print("Error: You are in a non-existent room. Aborting.")
                break
                
            current_room.describe()
            command = input("> ").lower().strip()
            
            # CHANGED: We pass the validated `current_room` object to the processor.
            self._process_command(command, current_room)

    # CHANGED: The method now accepts the `current_room` object.
    def _process_command(self, command, current_room):
        """
        Parses and acts on the user's command.

        Args:
            command (str): The command entered by the user.
            current_room (Room): The room the player is currently in.
        """
        parts = command.split()
        if not parts:
            print("Please enter a command.")
            return

        verb = parts[0]
        
        if verb == "quit":
            self.is_running = False
            print("You decide to end your adventure.")
        elif verb == "help":
            self.show_help()
        elif verb == "go":
            if len(parts) > 1:
                direction = parts[1]
                # CHANGED: We pass the validated `current_room` to the move logic.
                self._move_player(direction, current_room)
            else:
                print("Go where? (e.g., 'go north')")
        else:
            print("I don't understand that command. Type 'help' for a list of commands.")

    # CHANGED: The method now accepts the `current_room` object, making it safer
    # and more efficient.
    def _move_player(self, direction, current_room):
        """
        Handles the logic for moving the player.
        
        Args:
            direction (str): The direction to move in.
            current_room (Room): The validated room object the player is in.
        """
        # REMOVED: No need to re-fetch the room. We use the one passed in.
        # current_room = self.world.get_room(self.player.current_location_id)
        
        if direction in current_room.exits:
            new_room_id = current_room.exits[direction]
            self.player.move(new_room_id)
        else:
            print("You can't go that way.")

    def show_intro(self):
        """Displays the welcome message and initial help text."""
        print("="*50)
        print("Welcome to the Text Adventure Game!")
        print("="*50)
        self.show_help()

    def show_help(self):
        """Displays the help message with available commands."""
        print("\n--- Available Commands ---")
        print("  go [direction] - Move to a new room (e.g., 'go north').")
        print("  help           - Show this help message.")
        print("  quit           - Exit the game.")
        print("--------------------------")