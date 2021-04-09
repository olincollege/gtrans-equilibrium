"""
Scraper for translationparty's "hot parties" section
"""
import random
import requests
from bs4 import BeautifulSoup


URL = "https://www.translationparty.com"
response = requests.get(URL)  # , proxies = proxies)
soup = BeautifulSoup(response.content, "html.parser")
parties = [party.getText()
           for party in soup.find(id="hotparties").find_all("a")]


def scraper_to_text(scraped_text, output):
    """
    Record a random sentence from a list of scraped text to a txt file.

    Args:
        scraped_text: a list of strings representing the scraped data
        output: a string representing the path of the file to be written
    """
    with open(output, "w") as file:
        file.write(random.choice(scraped_text))
