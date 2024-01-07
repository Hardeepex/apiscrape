import requests
from bs4 import BeautifulSoup
from lxml import html


def fetch_page(url):
    response = requests.get(url)
    return response.content

def parse_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup

def extract_content(soup, selector, xpath=False):
    if xpath:
        tree = html.fromstring(str(soup))
        return tree.xpath(selector)
    else:
        return soup.select(selector)
