# -*- coding: utf-8 -*-
"""
Part 4, Lesson 22: Project: Web Scraper

Author: dunamismax
Date: 06-15-2025

This file is a project that demonstrates how to perform web scraping.
It uses the `requests` library to fetch a webpage's content and the
`BeautifulSoup` library to parse and extract specific data from the HTML.
"""

'''
=====================================================================================
|                                   - LESSON START -                                  |
=====================================================================================

Welcome to one of the most powerful and practical applications of Python:
WEB SCRAPING.

WHAT IS WEB SCRAPING?
Web scraping is the automated process of extracting information and data from
websites. Instead of a human manually copying and pasting data from a webpage,
we write a script to do it for us. This is incredibly useful for gathering data
for analysis, monitoring changes on a site, or creating datasets.

THE TWO-STEP PROCESS:
1.  FETCHING: First, we need to get the raw HTML code of the webpage. For this,
    we'll use the `requests` library, which you saw in our API project.

2.  PARSING: Once we have the HTML, it's just a long string of text. It's not
    easy to work with. We need to PARSE it, which means turning the string into a
    structured object that we can easily navigate. For this, we will use a new,
    extremely popular library called BEAUTIFULSOUP.

BEAUTIFULSOUP is a Python library designed for pulling data out of HTML and XML
files. It provides simple, Pythonic ways of navigating, searching, and modifying
the parse tree.

A NOTE ON ETHICS:
Web scraping is a powerful tool, but it must be used responsibly.
- Always check a website's `robots.txt` file (e.g., `https://example.com/robots.txt`)
  to see what they permit.
- Do not send too many requests in a short time, as this can overload the
  website's server. Be a good web citizen.
- Respect copyrights and the website's terms of service.
For this lesson, we will use `http://quotes.toscrape.com`, a website specifically
designed for practicing web scraping.

--- SETUP: THIS PROJECT REQUIRES EXTERNAL LIBRARIES ---

This project demonstrates the professional workflow we learned in the last lesson.
Follow these steps in your terminal:

1.  Create a new project folder and navigate into it:
    `mkdir web_scraper_project && cd web_scraper_project`

2.  Create a virtual environment:
    `python -m venv venv`

3.  Activate the virtual environment:
    (macOS/Linux): `source venv/bin/activate`
    (Windows):     `.\\venv\\Scripts\\activate`

4.  Install the necessary packages (requests and beautifulsoup4):
    `pip install requests beautifulsoup4`
    NOTE: The library is imported as `bs4`, but installed as `beautifulsoup4`.

5.  Save your dependencies:
    `pip freeze > requirements.txt`

6.  Now, create this Python file (`22_project_web_scraper.py`) inside the
    `web_scraper_project` folder and you're ready to go!
'''

# We must import the libraries we installed.
# `requests` is for fetching the webpage.
# `BeautifulSoup` is for parsing the HTML. It's located inside the `bs4` package.
import requests
from bs4 import BeautifulSoup


# The main execution block starts here.
if __name__ == "__main__":
    
    # --- Part 1: Fetching the Webpage ---
    # We define the URL of the site we want to scrape.
    URL = "http://quotes.toscrape.com/"
    print(f"--- Fetching webpage: {URL} ---")

    try:
        # Use requests.get() to download the HTML content.
        response = requests.get(URL)

        # It's good practice to check if the request was successful.
        # A status code of 200 means "OK".
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

        html_content = response.text
        print("Successfully fetched the webpage HTML.")

    except requests.exceptions.RequestException as e:
        # This is a general exception for the requests library. It will catch
        # connection errors, timeouts, etc.
        print(f"Error fetching the webpage: {e}")
        # If we can't get the page, there's no point in continuing.
        exit()


    # --- Part 2: Parsing the HTML with BeautifulSoup ---
    # Now we create a BeautifulSoup object, which represents the parsed document.
    # Arguments:
    # 1. The HTML content we fetched.
    # 2. The parser we want to use. 'html.parser' is built-in with Python.
    print("\n--- Parsing HTML with BeautifulSoup ---")
    soup = BeautifulSoup(html_content, "html.parser")
    print("HTML parsed successfully. We can now search for data.")


    # --- Part 3: Finding and Extracting Data ---
    # This is the core of scraping. We need to inspect the webpage's HTML
    # (using the "Inspect" tool in a web browser like Chrome or Firefox) to
    # find the tags and classes that contain the data we want.
    #
    # On quotes.toscrape.com, each quote is contained within a <div> element
    # that has the CSS class "quote".
    
    print("\n--- Finding all quote elements ---")
    
    # `soup.find_all()` returns a list of all elements that match our query.
    # We're looking for all 'div' tags with a class of 'quote'.
    # NOTE: We use `class_` with an underscore because `class` is a reserved
    # keyword in Python.
    quote_elements = soup.find_all('div', class_='quote')
    print(f"Found {len(quote_elements)} quotes on the page.")
    
    # We will store our structured data in a list of dictionaries.
    scraped_quotes = []

    # Now, we loop through each element we found.
    for quote_element in quote_elements:
        # Within each 'div', the text is in a <span> with class="text".
        # `.find()` gets the *first* matching element.
        # `.get_text()` extracts the text content from the element.
        text = quote_element.find('span', class_='text').get_text(strip=True)
        
        # The author is in a <small> tag with class="author".
        author = quote_element.find('small', class_='author').get_text(strip=True)
        
        # The tags are inside a <div> with class="tags". Inside that div, each
        # tag is an <a> tag. So we find the container first.
        tags_container = quote_element.find('div', class_='tags')
        
        # Then we find all the 'a' tags within that container.
        tag_elements = tags_container.find_all('a', class_='tag')
        
        # We can use a LIST COMPREHENSION to extract the text from each tag element.
        # This is a clean and "Pythonic" way to build a list.
        tags = [tag.get_text(strip=True) for tag in tag_elements]
        
        # Store the extracted data in a dictionary.
        scraped_quotes.append({
            "text": text,
            "author": author,
            "tags": tags
        })
        

    # --- Part 4: Displaying the Scraped Data ---
    print("\n--- Displaying Scraped Quotes ---")
    if not scraped_quotes:
        print("No quotes were scraped.")
    else:
        # Loop through our list of dictionaries and print the data nicely.
        for i, quote in enumerate(scraped_quotes, 1):
            print(f"\nQuote #{i}")
            print(f"  Text: {quote['text']}")
            print(f"  Author: {quote['author']}")
            # The join() string method is a great way to format a list for printing.
            print(f"  Tags: {', '.join(quote['tags'])}")

'''
=====================================================================================
|                                    - LESSON END -                                   |
=====================================================================================

SUMMARY:

Congratulations! You have just built a functional web scraper. This project
combined several key skills: virtual environments, installing packages with pip,
fetching web data with `requests`, and parsing HTML with `BeautifulSoup`.

Key Concepts Reinforced:
1.  WEB SCRAPING is a two-step process: fetching (getting HTML) and parsing
    (extracting data).
2.  The `requests` library is used for fetching.
3.  The `BeautifulSoup` library is the standard for parsing HTML in Python.
4.  You create a `soup` object by passing it HTML content.
5.  You use methods like `find_all('tag', class_='classname')` to locate the
    data you need.
6.  `find()` gets the first match, while `find_all()` gets all matches.
7.  `.get_text()` extracts the clean text from within an HTML element.
8.  Always remember to scrape ethically and responsibly.

HOW TO RUN THIS CODE:

1.  Make sure you have followed the setup instructions at the top of this file
    (created a folder, a venv, and installed packages).
2.  Activate your virtual environment:
    (macOS/Linux): `source venv/bin/activate`
    (Windows):     `.\\venv\\Scripts\\activate`
3.  Run the file from your terminal:
    `python 22_project_web_scraper.py`
4.  You should see the script fetch the webpage and then print out the formatted
    quotes it found.
'''