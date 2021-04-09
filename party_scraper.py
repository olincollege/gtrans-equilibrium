import requests
from bs4 import BeautifulSoup
import random

url = "https://www.translationparty.com"
response = requests.get(url)#, proxies = proxies)
soup = BeautifulSoup(response.content, "html.parser")
parties = [party.getText() for party in soup.find(id="hotparties").find_all("a")]

def scraper_to_text(scraped_text, output):
    """
    Record the a random sentence from a scraped text to a txt file.

    Args:
        scraped_text ([type]): [description]
        file ([type]): [description]
    """
    with open(output, "w") as file:
        file.write(random.choice(scraped_text))