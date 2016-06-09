#! /usr/bin/env python
import requests
from bs4 import BeautifulSoup, SoupStrainer
from IPython import embed

prefix = 'https://en.wikipedia.org/wiki/'

def findlinks(page):
    results = []
    page = requests.get(prefix + page).text
    for link in BeautifulSoup(page, "html.parser", parse_only=SoupStrainer('a')):
        if link.has_attr('href'):
            if link['href'].startswith('/wiki') and ':' not in link['href']:
                results.append(link['href'][6:])
    return set(results)

if __name__ == '__main__':
    print(findlinks('Archaea'))
