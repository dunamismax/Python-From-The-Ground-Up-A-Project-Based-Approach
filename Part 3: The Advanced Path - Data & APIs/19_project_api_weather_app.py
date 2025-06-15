# -*- coding: utf-8 -*-
"""
Part 3, Lesson 19: Project: API Weather App

Author: dunamismax
Date: 06-15-2025

This file is our first project that connects to the internet! We will
build a simple command-line weather application that fetches and displays
live weather data from a real-world API using the `requests` library.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

PROJECT GOAL:
Build an application that asks the user for a city name, fetches the current
weather for that city from a web API, and displays the information.

WHAT IS AN API?
API stands for Application Programming Interface. In simple terms, it's a way
for different software programs to communicate with each other. A web API
allows our Python script to request data from a server on the internet.

Think of it like ordering food at a restaurant:
1.  You (the CLIENT) look at a menu (the API documentation) to see what you can order.
2.  You give your order (an API REQUEST) to the waiter (the API ENDPOINT).
3.  The kitchen (the SERVER) prepares your food.
4.  The waiter brings your food back (the API RESPONSE), usually in a structured
    format like JSON.

THE `requests` LIBRARY:
To make these API requests in Python, we use a third-party library called
`requests`. It's not part of the standard library, so we must install it first.

*** IMPORTANT: PREREQUISITES ***

1. INSTALL THE `requests` LIBRARY:
   Open your terminal or command prompt and run this command:
   `pip install requests`

2. GET A FREE API KEY:
   Most APIs require an API KEY to track usage and prevent abuse. It's a unique
   code that identifies your application. We will use the OpenWeatherMap API.

   a. Go to: https://openweathermap.org/
   b. Sign up for a free account.
   c. Navigate to the "API keys" tab in your account dashboard.
   d. A default key will be generated for you. Copy this key.
   e. It may take a few minutes to a couple of hours for a new key to become active.

   WARNING: Treat your API key like a password! Do not share it publicly or
   commit it to a public repository like GitHub.
'''

# We import the `requests` library to handle our web requests.
import requests

# The main execution block starts here.
if __name__ == "__main__":
    
    # --- Part 1: Configuration ---
    # It's good practice to put configuration variables at the top.
    
    # PASTE YOUR API KEY HERE! Replace the placeholder string with your actual key.
    # The program WILL NOT WORK without a valid key.
    API_KEY = "YOUR_API_KEY_GOES_HERE"
    
    # This is the base URL for the weather API endpoint we are using.
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    
    # We must check if the user has replaced the placeholder key.
    if API_KEY == "YOUR_API_KEY_GOES_HERE":
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! ERROR: You have not set your API_KEY.            !!!")
        print("!!! Open this file and replace the placeholder text. !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        # --- Part 2: Get User Input ---
        # Ask the user for the city they want the weather for.
        city = input("Enter the name of a city: ")
        
        # --- Part 3: Making the API Request ---
        # We construct the full URL with "parameters". Parameters are added to a URL
        # after a `?` and are used to send information with our request.
        # `q` is the parameter for the city name.
        # `appid` is the parameter for our API key.
        # `units=metric` tells the API to return temperature in Celsius.
        request_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        
        print(f"\nFetching weather data for {city}...")
        
        # Now, we use a `try...except` block to gracefully handle potential errors,
        # such as no internet connection or an invalid city name.
        try:
            # `requests.get()` sends an HTTP GET request to the specified URL.
            response = requests.get(request_url)
            
            # The `raise_for_status()` method is a great helper. If the request
            # resulted in an error (e.g., 404 Not Found, 401 Unauthorized),
            # it will automatically raise an exception and stop the program here.
            response.raise_for_status()
            
            # --- Part 4: Parsing the JSON Response ---
            # If the request was successful (status code 200 OK), the response
            # object contains the data from the server. The `.json()` method
            # automatically parses the JSON text into a Python dictionary.
            data = response.json()
            
            # To understand the data, it's helpful to print it out during development.
            # Uncomment the line below to see the full dictionary structure!
            # print(data)
            
            # --- Part 5: Extracting and Displaying Data ---
            # Now we navigate the dictionary to pull out the specific pieces
            # of information we care about. This structure is defined by the API.
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print("\n--- Current Weather ---")
            print(f"Description: {weather_description.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Feels Like:  {feels_like}°C")
            print(f"Humidity:    {humidity}%")
            print(f"Wind Speed:  {wind_speed} m/s")
            print("-----------------------")

        except requests.exceptions.HTTPError as err:
            # This block catches specific HTTP errors.
            if err.response.status_code == 404:
                print(f"Error: City '{city}' not found. Please check the spelling.")
            elif err.response.status_code == 401:
                print("Error: Invalid API key. Please check your key in the script.")
            else:
                print(f"An HTTP error occurred: {err}")
        except requests.exceptions.RequestException as err:
            # This is a general catch-all for other `requests` issues (e.g., network error).
            print(f"An error occurred: {err}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations! You've built a real, working application that connects to the
internet and uses live data. This is a massive step forward.

In this project, you combined many skills:
1.  PACKAGE MANAGEMENT: You installed a third-party library (`requests`) using `pip`.
2.  API COMMUNICATION: You learned what an API is and made a GET request to a real
    web server.
3.  JSON PARSING: You used the `.json()` method to effortlessly convert a JSON
    response into a Python dictionary.
4.  DATA HANDLING: You navigated a nested dictionary to extract the exact data you
    needed.
5.  ERROR HANDLING: You used `try...except` to make your program robust and handle
    potential issues like network failures or bad user input.

You can now connect your Python programs to the vast world of data available on
the internet. Almost every major web service (Twitter, Spotify, Google Maps, etc.)
offers an API you can interact with using these same techniques.

HOW TO RUN THIS CODE:

1.  Make sure you have installed the `requests` library: `pip install requests`
2.  Save this file as `19_project_api_weather_app.py`.
3.  **IMPORTANT**: Open the file and replace `"YOUR_API_KEY_GOES_HERE"` with your
    actual API key from OpenWeatherMap.
4.  Open a terminal or command prompt.
5.  Navigate to the directory where you saved this file.
6.  Run the file with the command: `python 19_project_api_weather_app.py`
'''