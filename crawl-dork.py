import requests
from bs4 import BeautifulSoup

def web_bot(keywords, file_name):
    # Keep track of visited URLs to avoid visiting the same URL multiple times
    visited = set()

    # Queue of URLs to be processed
    queue = []

    # Starting URL
    queue.append("https://www.google.com/search?q=" + keywords)

    while queue:
        # Get the URL from the queue
        url = queue.pop(0)

        # Skip the URL if it has already been processed
        if url in visited:
            continue
        visited.add(url)

        # Get the HTML content of the URL
        try:
            response = requests.get(url)
        except:
            continue

        # Extract the URLs from the HTML content
        soup = BeautifulSoup(response.content, "html.parser")
        links = [link.get("href") for link in soup.find_all("a")]

        # Append the URLs to the queue
        for link in links:
            if "http" in link and link not in visited:
                queue.append(link)

        # Check if the URL contains the keywords
        if keywords in response.text:
            # Append the URL to the text file
            with open(file_name, "a") as file:
                file.write(url + "\n")
