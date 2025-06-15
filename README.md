# Python From The Ground Up 

<p align="left">
  <b>A complete, open-source curriculum that teaches you Python by building a versatile portfolio of real-world tools and applications.</b>
</p>
<p align="left">
  This course uses a unique, hands-on teaching method: <b>the lesson is in the code</b>. You'll learn every concept from structured comments inside a single, runnable Python file for each topic.
</p>
<p align="center">
  <a href="https://www.python.org/downloads/release/python-3110/"><img src="https://img.shields.io/badge/Language-Python%203.11+-blue.svg" alt="Python 3.11+"></a>
  <a href="https://pip.pypa.io/en/stable/"><img src="https://img.shields.io/badge/Packages-pip-green.svg" alt="pip"></a>
  <a href="https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"></a>
  <a href="https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach/stargazers"><img src="https://img.shields.io/github/stars/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach?style=social" alt="GitHub Stars"></a>
</p>

---

Welcome to the ultimate learn-by-doing course for the Python programming language! This isn't just a tutorial; it's a complete educational journey designed to build deep, practical knowledge from absolute zero. We start with the basics—assuming you've never written a line of code—and guide you to building an impressive portfolio of projects, including a weather app that calls a live API, a web scraper, and a full text-based RPG.

> Learning Python is about more than just syntax; it's about learning to think like a programmer. This course teaches you to write clean, efficient, and "Pythonic" code, empowering you to build anything from a simple script to a complex application with confidence and clarity.

## ✨ Why This Approach?

*   📖 **Learn Directly In The Code**: Forget switching between a book and your editor. Every lesson is taught directly within the comments of a single, runnable Python file. The code *is* the textbook.
*   👨‍💻 **True Beginners Welcome**: This course has zero prerequisites. We'll guide you through your first `print("Hello, World!")` before gradually introducing the powerful concepts that make Python a world-class language.
*   🚀 **From "Hello, World!" to Web APIs & Data Viz**: The curriculum is carefully structured to build your skills layer by layer. You'll master Python fundamentals, then use them to interact with files, fetch data from the internet, visualize information, and build multi-file applications.
*   🛠️ **Build a Versatile Portfolio**: The entire course is oriented around practical projects. Every concept, from `lists` to `classes`, is a building block for tools like a password generator, a contact book, a web scraper, and a data plotter.
*   💪 **Master Professional Practices**: We don't just teach syntax. You will gain true confidence with Object-Oriented Programming (OOP), professional dependency management with virtual environments, automated testing, and structuring larger projects.
*   🌍 **Open Source & Community Driven**: This curriculum is for everyone. Contributions, suggestions for improvement, bug fixes, and new project ideas are highly encouraged!

---

## 💻 Tech Stack & Prerequisites

You don't need any programming knowledge to start, but you will need a few standard, free tools.

*   **Python** (version 3.11+ is recommended).
*   **pip**, the Python Package Installer (this is usually included with your Python installation).
*   **Git** for cloning this repository to your computer.
*   A good Text Editor or IDE (Visual Studio Code with the Python extension is a fantastic, free choice).

---

## 🚀 How to Use This Course

Each lesson folder contains a single `.py` file (or multiple files for larger projects). This file is both the complete, runnable program and the full lesson text.

1.  **Read the Lesson:** Navigate to a lesson folder (e.g., `Part1_Python_Basics/01_HelloWorld/`) and open the `1_hello_world.py` file. Read the comments from top to bottom to understand the concepts.

2.  **Run the Code:** To see the lesson's concepts in action, you'll need to run the Python script from your terminal.

    First, clone the repository (you only need to do this once):
    ```sh
    git clone https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach.git
    cd Python-From-The-Ground-Up-A-Project-Based-Approach/
    ```

    Then, for each lesson, navigate to its folder and use the Python interpreter to run the file.
    ```sh
    # Example for the first lesson
    cd Python-From-The-Ground-Up-A-Project-Based-Approach/Part\ 1:\ The\ Beginner\ Path\ -\ Python\ Basics/

    # Run the Python script
    # On most modern systems:
    python 1_hello_world.py

    # On some systems, you may need to use python3:
    python3 1_hello_world.py
    ```
    *Note: Later projects will require installing external packages. In those cases, instructions will be provided on how to use `pip`.*

---

## 📚 The Curriculum

The curriculum is divided into five parts, taking you from a blank text file to a proficient Python developer capable of building complex and useful applications.

<details>
<summary><strong>Part 1: The Beginner Path - Python Basics</strong></summary>
<br>
<i>(Focus: Core language syntax, data structures, and logic, taught entirely within single-file console applications.)</i>

| Lesson                           | Key Concepts                                 | Description                                                              |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| `1_hello_world.py`               | `print()`, comments, interpreter             | The essential first step: running your very first Python program.        |
| `2_variables_and_types.py`       | `str`, `int`, `float`, `bool`, dynamic typing| Learn to store, manage, and work with different kinds of information.    |
| `3_user_input_and_strings.py`    | `input()`, f-strings, `.lower()`, `.strip()` | Make your programs interactive by reading and manipulating user input.   |
| `4_operators_and_comparisons.py` | `+`, `/`, `%`, `==`, `!=`, `and`, `or`       | Perform calculations, comparisons, and make logical decisions.           |
| `5_conditional_logic.py`         | `if`, `elif`, `else`, indentation            | Give your program a brain by letting it execute code based on conditions.|
| `6_lists_the_python_workhorse.py`| Indexing, slicing, `.append()`, `.pop()`     | Manage ordered collections of data, Python's most versatile data type.   |
| `7_loops.py`                     | `for` loops, `while` loops                   | Teach your program to perform repetitive tasks and iterate over data.    |
| `8_functions.py`                 | `def`, arguments, `return`, docstrings       | Organize code into clean, reusable, and modular blocks—a core concept.   |
| `9_dictionaries_key_value_pairs.py`| `{key: value}`, accessing with keys        | Store and retrieve data efficiently using unique keys instead of indices.|

</details>

<details>
<summary><strong>Part 2: The Intermediate Path - Building Tools</strong></summary>
<br>
<i>(Focus: Interacting with the system, handling errors, and learning Object-Oriented Programming.)</i>

| Lesson                             | Key Concepts                                 | Description                                                              |
| ---------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| `10_files_and_the_os.py`           | `with open(...)`, `os` module                | Persist data beyond program execution by reading from and writing to files.|
| `11_modules_and_pip.py`            | `import`, standard library, `pip` install    | Expand Python's power with built-in modules and third-party packages.    |
| `12_exception_handling.py`         | `try`, `except` block                        | Write robust, professional code that can handle unexpected errors gracefully.|
| `13_project_password_generator.py` | **Project:** `random` module, loops, functions| Build your first useful tool: a customizable strong password generator.    |
| `14_classes_and_oop_basics.py`     | `class`, `__init__()`, `self`, methods       | Intro to Object-Oriented Programming, the paradigm of modern software.   |
| `15_project_contact_book.py`       | **Project:** Classes, dictionaries, file I/O | Build an application to create, manage, and save contacts to a file.     |

</details>

<details>
<summary><strong>Part 3: The Advanced Path - Data & APIs</strong></summary>
<br>
<i>(Focus: Advanced data structures and interacting with web services.)</i>

| Lesson                              | Key Concepts                                 | Description                                                              |
| ----------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| `16_advanced_data_structures.py`    | `tuple` (immutability), `set` (uniqueness)   | Learn about immutable sequences and efficient collections of unique items. |
| `17_list_and_dict_comprehensions.py`| `[x for x in list]`, `{k:v for k,v in d}`    | Write elegant, efficient, and highly readable "Pythonic" loops.        |
| `18_working_with_json.py`           | `json` module, `load()`, `dump()`            | Master JSON, the universal language of web APIs and data exchange.       |
| `19_project_api_weather_app.py`     | **Project:** `requests` library, JSON parsing| Connect to the internet to fetch and display live data from a real API.  |
| `20_lambdas_and_functional_tools.py`| `lambda`, `map()`, `filter()`                | Explore functional programming concepts for concise, powerful one-liners.|

</details>

<details>
<summary><strong>Part 4: The Expert Path - Best Practices & The Ecosystem</strong></summary>
<br>
<i>(Focus: Professional development tools, testing, and data visualization.)</i>

| Lesson                                     | Key Concepts                                   | Description                                                              |
| ------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------ |
| `21_virtual_environments_and_requirements.py`| `venv`, `pip freeze`, `requirements.txt`       | Learn the professional standard for managing project dependencies.       |
| `22_project_web_scraper.py`                | **Project:** `requests`, `BeautifulSoup`       | Build a powerful tool to automatically extract information from websites.|
| `23_generators_and_iterators.py`           | `yield` keyword, memory efficiency             | Create memory-efficient data sequences for handling large datasets.      |
| `24_testing_with_pytest.py`                | `pytest`, assertions, test functions         | Intro to automated testing to ensure your code is correct and reliable.  |
| `25_project_csv_data_plotter.py`           | **Project:** `matplotlib`, `csv` module      | Read data from a standard CSV file and create a visual chart from it.  |

</details>

<details>
<summary><strong>Part 5: Expert Systems & Application Development</strong></summary>
<br>
<i>(Focus: Building large, multi-file applications and preparing them for distribution.)</i>

| Lesson                                     | Key Concepts                                 | Description                                                              |
| ------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------------------ |
| `26_structuring_a_multi_file_project/`     | Project structure, `main.py`, modules      | Learn how to organize code for large, scalable, and maintainable apps.   |
| `27_intro_to_gui_with_tkinter.py`          | `tkinter`, widgets, event loops              | A first look at building graphical user interfaces for desktop apps.     |
| `28_capstone_text_adventure_game/`         | **Final Capstone Project**                   | A multi-file text RPG using classes, JSON, and advanced project structure. |
| `29_packaging_your_project_with_pyproject.py`| `pyproject.toml`, `build`, `twine`         | A look at modern Python packaging to make your projects shareable.       |
| `30_what_next.py`                          | Guidance document                            | A commented guide to further learning paths in web dev, data science, etc. |

</details>

---

## ⭐ Show Your Support

If this course helps you become a better developer, please **give this repository a star!** It helps the project reach more aspiring programmers and encourages us to keep creating great, free educational content.

## 🤝 Connect & Contribute

This project is for the community. Have an idea for a new feature, a better way to explain a concept, or find a bug? Feel free to [open an issue](https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach/issues) or [submit a pull request](https://github.com/dunamismax/Python-From-The-Ground-Up-A-Project-Based-Approach/pulls)!

Connect with the author, **dunamismax**, on:

*   **Twitter:** [@dunamismax](https://twitter.com/dunamismax)
*   **Bluesky:** [@dunamismax.bsky.social](https://bsky.app/profile/dunamismax.bsky.social)
*   **Reddit:** [u/dunamismax](https://www.reddit.com/user/dunamismax)
*   **Discord:** `dunamismax`
*   **Signal:** `dunamismax.66`

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.