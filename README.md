# Web Scraping and File Handling with Python

In `web_scraping.py` Python script allows you to perform web scraping of Google search results. It fetches and displays the title and URL of the first search result and saves this information in a text file.

## Code Explanation

The code uses the following libraries:

- `requests`: To send HTTP requests to Google.
- `BeautifulSoup` from `bs4`: To parse and navigate the HTML content of the Google search results.

__The main steps of the code are as follows:__

1. **Initialize an Empty List:** An empty list called `queries` is created to store user search queries.

2. **Get User Input:** The code enters a loop to get a user's search query via the `input` function. The user can enter multiple queries, and the loop continues until the user enters 'q' to quit.

3. **Send an HTTP Request to Google:** It sends an HTTP GET request to Google with the user's query using a user-agent header to simulate a web browser request.

4. **Extract Title and URL:** The code parses the HTML content of the search results using BeautifulSoup. It locates the title and URL of the first search result by navigating the HTML structure.

5. **Display Information:** It prints the title and URL in the terminal so the user can see the results.

6. **Save Information to a Text File:** The title and URL are saved in a text file called "results.txt" for future reference.

