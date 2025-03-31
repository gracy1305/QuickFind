import requests
from bs4 import BeautifulSoup

# Example URL to test
url = 'https://www.wikipedia.org'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the title of the page
title = soup.find('title').text
print(f"Title of the page: {title}")
