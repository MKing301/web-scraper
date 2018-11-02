"""This module scrapes a specific website using Beautiful Soup 4.

 The module will scrape the quote and the author of the quote from the
html text.
"""

from bs4 import BeautifulSoup
import requests

# Request to get text from web page
source = requests.get('http://quotes.toscrape.com/tag/inspirational/').text

# Pass source into Beautiful Soup and parse html
soup = BeautifulSoup(source, 'lxml')

# Obain first quote from the parsed html
quote = soup.find('div', class_='quote')

# Print formatted html quote
print(quote.prettify())
