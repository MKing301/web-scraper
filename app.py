"""This module scrapes a specific website using Beautiful Soup 4.

 The module will scrape the quote and the author of the quote from the
html text.
"""

from bs4 import BeautifulSoup
import requests
import csv

# Request to get text from web page
source = requests.get('http://quotes.toscrape.com/tag/inspirational/').text

# Pass source into Beautiful Soup and parse html
soup = BeautifulSoup(source, 'lxml')

csv_file = open('quotes.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Quote', 'Author'])

# Obain all quotes in the parsed html by looping through list of matching tags
for quote in soup.find_all('div', class_='quote'):

    # Obtain quote
    quote_text = quote.find('span', class_='text').text

    # Obtain auther of the quote
    quote_author = quote.find('small', class_='author').text

    csv_writer.writerow([quote_text, quote_author])
csv_file.close()
