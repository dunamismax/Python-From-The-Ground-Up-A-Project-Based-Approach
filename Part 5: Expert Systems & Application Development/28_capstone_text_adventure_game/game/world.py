# -*- coding: utf-8 -*-
"""
Part 5, Lesson 28: World Module

Author: dunamismax
Date: 06-15-2025

This module defines the Room and World classes, which handle the
game's environment and map data.
"""

import json

class Room:
    """
    Represents a single room or location in the game world.

    Attributes:
        id (str): The unique identifier for the room.
        name (str): The human-readable name of the room.
        description (str): A text description of the room.
        exits (dict): A dictionary mapping exit directions to other room IDs.
    """
    def __init__(self, room_id, name, description, exits):
        self.id = room_id
        self.name = name
        self.description = description
        self.exits = exits

    def describe(self):
        """Prints a full description of the room to the console."""
        print(f"\n--- {self.name} ---")
        print(self.description)
        
        # List the available exits
        available_exits = ", ".join(self.exits.keys())
        print(f"Exits: {available_exits}")


class World:
    """
    Manages the entire game world, loaded from a data file.

    Attributes:
        rooms (dict): A dictionary holding all Room objects, keyed by their ID.
        start_room_id (str): The ID of the room where the game begins.
    """
    def __init__(self, map_data_file):
        """
        Initializes the World by loading map data from a file.

        Args:
            map_data_file (str): The path to the JSON file containing map data.
        """
        self.rooms = {}
        self.start_room_id = None
        self._load_map(map_data_file)

    def _load_map(self, map_data_file):
        """
        Private method to load and parse the map data from a JSON file.
        """
        try:
            with open(map_data_file, 'r') as f:
                map_data = json.load(f)
            
            self.start_room_id = map_data["start_room_id"]
            
            # Create a Room object for each room defined in the JSON file
            for room_id, room_info in map_data["rooms"].items():
                self.rooms[room_id] = Room(
                    room_id=room_id,
                    name=room_info["name"],
                    description=room_info["description"],
                    exits=room_info["exits"]
                )
        except FileNotFoundError:
            print(f"Error: Map file not found at '{map_data_file}'")
            exit() # Exit the program if the map can't be loaded
        except json.JSONDecodeError:
            print(f"Error: Could not decode JSON from '{map_data_file}'")
            exit()

    def get_room(self, room_id):
        """
        Retrieves a Room object by its ID.

        Args:
            room_id (str): The ID of the room to retrieve.

        Returns:
            Room: The Room object, or None if the ID is not found.
        """
        return self.rooms.get(room_id)