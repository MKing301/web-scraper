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

# Obtain text of first quote
quote_text = quote.find('span', class_='text').text

# Obtain auther of first quote
quote_author = quote.find('small', class_='author').text

# Print quote
print(quote_text)

# Print author of quote
print(quote_author)
