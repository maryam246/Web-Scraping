import requests
from bs4 import BeautifulSoup

# Initialize an empty list to store the queries.
queries = []

with open("results.txt", "w") as f:
    while True:
        # Get a user's search query.
        query = input("Enter a search query (or 'q' to quit): ")

        # Check if the user wants to quit.
        if query.lower() == 'q':
            break

        # Store the query in the list.
        queries.append(query)

        # Send an HTTP request to Google.
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
        }

        response = requests.get(f"https://www.google.com/search?q={query}", headers=headers)

        # Extract the title and URL of the first search result.
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("div", {"class": "tF2Cxc"})

        if result is not None:
            title = result.find("h3").text
            url = result.find("a")["href"]
            # Google search results may include a prefix like "/url?q=", so we remove it.
            if url.startswith("/url?q="):
                url = url[7:]
        else:
            title = "No results found."
            url = ""

        # Display the title and URL in the terminal.
        print(f"Title: {title}")
        print(f"URL: {url}")
        print()

        # Save the title and URL in the file.
        f.write(f"Query: {query}\n")
        f.write(f"Title: {title}\n")
        f.write(f"URL: {url}\n\n")
