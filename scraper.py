# Basic web scraper for article titles
# Brandon Dawson
# 02/06/2024

import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    # Send an HTTP request to the specified URL
    response = requests.get(url)
    # Check for a successful request code(200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract article titles (adjust selector based on the website labeling)
        titles = soup.select('.home-title')
        
        # Print the titles
        for title in titles:
            print(title.text)
            
    else:
        print(f"Error: Unable to retrieve content")
        
url_to_scrape = 'https://thehackernews.com/'
scrape_news_titles(url_to_scrape)