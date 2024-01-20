import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_page(url, script_directory):
    try:
        # Send an HTTP GET request to the URL
        r = requests.get(url)
        r.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(r.content, 'html.parser')

        # Save the HTML content to a file
        save_path = os.path.join(script_directory, f"{url.replace('://', '_').replace('/', '_')}.html")
        with open(save_path, 'w', encoding='utf-8') as html_file:
            html_file.write(str(soup))

        print(f"HTML content saved to {save_path}")

        # Extract links from the page and scrape them recursively
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            print(f"Following link: {next_url}")
            scrape_page(next_url, script_directory)

    except requests.exceptions.RequestException as e:
        print(f"Error scraping {url}: {e}")

def scrap():
    # find the dir of the link file "urls.txt"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, 'urls.txt')
    
    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Iterate through each line and scrape the content of the linked pages
    for line in lines:
        url = line.strip()
        print(f"Scraping {url}")
        scrape_page(url, script_directory)

# Call the function to execute the code
scrap()
