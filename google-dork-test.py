import requests
from bs4 import BeautifulSoup
import time

# List of all available dorks
dorks = ["inurl:filetype:", "site:", "intext:", "intitle:", "ext:", "link:"]

# Read hostnames from file
with open('hostnames.txt', 'r') as file:
    hostnames = file.readlines()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# Iterate through hostnames and dorks
for hostname in hostnames:
    hostname = hostname.strip()
    for dork in dorks:
        query = dork + hostname
        url = "https://www.google.com/search?q=" + query
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extract search results from page
        results = soup.find_all('div', {'class': 'g'})
        for result in results:
            # Extract title and link of each search result
            title = result.find('h3').text
            link = result.find('a')['href']
            print(f'{title}: {link}')
        time.sleep(5) # introduce a delay of 5 seconds between requests
