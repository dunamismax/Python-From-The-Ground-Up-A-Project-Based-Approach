# -*- coding: utf-8 -*-
"""
Part 5, Lesson 28: Player Module

Author: dunamismax
Date: 06-15-2025

This module defines the Player class for the text adventure game.
"""

class Player:
    """
    Represents the player in the game.

    Attributes:
        current_location_id (str): The ID of the room the player is currently in.
    """
    def __init__(self, start_location_id):
        """
        Initializes a Player object.

        Args:
            start_location_id (str): The ID of the room where the player starts.
        """
        self.current_location_id = start_location_id
        # In a more advanced game, you could add inventory, health, etc. here.
        # self.inventory = []
        # self.health = 100

    def move(self, new_location_id):
        """
        Updates the player's location to a new room.

        Args:
            new_location_id (str): The ID of the new room.
        """
        self.current_location_id = new_location_id
        print("You move to a new location.")