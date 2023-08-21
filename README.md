The provided code is a Python script that uses the Tkinter library for creating a graphical user interface (GUI) application and the Selenium and BeautifulSoup libraries for web scraping. The purpose of the application is to search for films on a movie website ("https://kinobase.org/films") based on user input and display the links to the found films in a text box. Here's a breakdown of the code:

1. Import Statements:
   - `tkinter as tk`: Imports the Tkinter library for GUI components.
   - `webdriver` and related modules from `selenium`: Imports Selenium for web automation and interaction.
   - `BeautifulSoup` from `bs4`: Imports BeautifulSoup for parsing HTML.

2. `search_films()` Function:
   - This function is called when the "Найти" ("Find") button is clicked.
   - Retrieves the search query from the input entry field.
   - Clears the existing content in the result text box.
   - Initiates a headless Chrome browser using Selenium with specified options.
   - Navigates to the movie website and performs a search using the user's query.
   - Extracts film links from the search results using BeautifulSoup.
   - Inserts the found links into the result text box.

3. GUI Setup:
   - Creates a Tkinter root window titled "Поиск фильмов" ("Search for Films").
   - Defines GUI components: label, entry field, search button, and result text box.
   - Packs these components to arrange them in the window layout.

4. Main Loop:
   - Starts the Tkinter main event loop to run the GUI application.

The GUI allows users to enter a search query for films, initiates a headless browser to interact with the movie website, extracts film links using BeautifulSoup, and displays the links in the result text box. Any errors during the process are also displayed in the result text box.
