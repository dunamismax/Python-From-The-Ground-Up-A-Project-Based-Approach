# Lesson 28: Capstone Project - Text Adventure Game

## Welcome to the Capstone!

This project is the culmination of everything you have learned in this course. We will build a complete, multi-file text adventure game. This project ties together:

*   **Object-Oriented Programming (OOP):** We'll use classes to model the game's components (`Player`, `Room`, `World`, `GameEngine`).
*   **Multi-File Project Structure:** We'll organize our code into logical modules within a `game/` package, just like in a professional application.
*   **Data-Driven Design:** The entire game world (rooms, descriptions, connections) will be loaded from an external `game_data.json` file. This is a powerful concept that separates your game's *content* from its *logic*.
*   **Core Python Skills:** The game is driven by a main loop, user input, conditional logic, and data structures like dictionaries and lists.

## The Goal

We are building a simple, expandable text adventure game. The player will be able to move between different rooms by typing commands like `go north`. They can also type `help` for instructions and `quit` to exit.

## Project Structure Breakdown

Our project is organized for clarity and scalability. Here's what each file does:
Use code with caution.
Markdown
28_capstone_text_adventure_game/
├── main.py
├── README.md
├── game_data.json
└── game/
├── init.py
├── engine.py
├── player.py
└── world.py

*   **`README.md` (This file):** Your guide to the project.
*   **`main.py`:** The application's entry point. Its only job is to start the game engine. It's the file you will run.
*   **`game_data.json`:** A database for our world. It defines all the rooms, their descriptions, and how they connect. By editing this file, you can change the entire game world without touching the Python code!
*   **`game/`:** A Python package that contains all our game logic.
    *   **`__init__.py`:** Makes the `game/` folder a package.
    *   **`player.py`:** Defines the `Player` class, which tracks the player's state (like their current location).
    *   **`world.py`:** Defines the `Room` and `World` classes. It's responsible for loading the map from the JSON file and managing the collection of rooms.
    *   **`engine.py`:** The heart of the game. The `GameEngine` class contains the main game loop, processes user commands, and coordinates the `Player` and `World` objects.

## How it All Works: The Flow of Logic

1.  You run `python main.py`.
2.  `main.py` creates an instance of the `GameEngine` from `game/engine.py`.
3.  The `GameEngine`'s constructor (`__init__`) does two things:
    *   It creates a `World` object (from `game/world.py`), passing it the `game_data.json` file path.
    *   The `World` object opens the JSON file, reads all the room data, and creates a `Room` object for each one.
    *   The `GameEngine` then creates a `Player` object (from `game/player.py`), placing them in the starting room defined by the `World`.
4.  `main.py` calls the `run()` method on the `GameEngine` instance.
5.  The `run()` method starts the main game loop. In each cycle, it:
    *   Looks at the player's current location.
    *   Describes the current room to the player.
    *   Asks for a command (e.g., `go north`).
    *   Processes the command, updating the player's location or exiting the game.
6.  The loop continues until the player types `quit`.

This **separation of concerns** makes the project easy to understand, debug, and expand.

## How to Run the Game

1.  Make sure you are in this `28_capstone_text_adventure_game/` directory in your terminal.
2.  Run the main entry point script:
    `python main.py`
    (or `python3 main.py` on some systems)

## How to Extend the Game

This game is a foundation. Here are some ideas for how you could expand it:

*   Add items to rooms and an inventory to the `Player` class.
*   Create `look` and `get <item>` commands.
*   Add NPCs (Non-Player Characters) or monsters to rooms.
*   Create a `fight` command.
*   Add locked doors that require a key from the player's inventory.