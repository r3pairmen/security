import requests
from termcolor import colored
import urllib3

# Disable SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# List of AEM endpoints to check for
aem_endpoints = [
    "/libs/cq/core/content/welcome.html",
    "/libs/granite/core/content/login.html",
    "/libs/wcm/core/content/siteadmin.html",
    "/libs/cq/search/content/querydebug.html",
    "/libs/granite/core/content/login/favicon.ico"
]

# Open the file containing the URLs to check
with open('urls.txt', 'r') as f:
    urls = f.readlines()

# Loop through each URL in the file
for url in urls:
    url = url.strip()
    try:
        # Make a GET request to the URL, ignoring SSL certificate verification and setting a timeout of 30 seconds
        response = requests.get(url, verify=False, timeout=30)

        # Check if any of the AEM endpoints or the phrase "Welcome to Adobe Experience Manager" are present in the response text
        aem_found = False
        for endpoint in aem_endpoints:
            if endpoint in response.text:
                aem_found = True
                # If an AEM endpoint is found, print a message saying the website is running AEM and highlight the "running" status in green
                print(f"{url}: {colored('running', 'green')} ({endpoint})")
                break
        if not aem_found and "Welcome to Adobe Experience Manager" in response.text:
            aem_found = True
            # If the phrase "Welcome to Adobe Experience Manager" is found, print a message saying the website is running AEM and highlight the "running" status in green
            print(f"{url}: {colored('running', 'green')} (Welcome message)")

        # If no AEM endpoint or the phrase "Welcome to Adobe Experience Manager" is found, print a message saying the website is not running AEM and highlight the "not running" status in red
        if not aem_found:
            print(f"{url}: {colored('not running', 'red')}")

    except requests.exceptions.Timeout:
        # If the request times out, assume the website is not running AEM and print a message highlighting the "not running" status in red
        print(f"{url}: {colored('not running', 'red')} (unresponsive)")

    except requests.exceptions.SSLError:
        # If there is an SSL verification error, assume the website is not running AEM and print a message highlighting the "not running" status in red
        print(f"{url}: {colored('not running', 'red')} (SSL verification error)")

    except:
        # If there is any other error, assume the website is not running AEM and print a message highlighting the "not running" status in red
        print(f"{url}: {colored('not running', 'red')} (error)")
