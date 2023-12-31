import requests
from bs4 import BeautifulSoup
from lxml import html


def fetch_html(url):
    response = requests.get(url)
    return response.content

def parse_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def select_elements(soup, selector):
    elements = soup.select(selector)
    return elements

def xpath_elements(soup, xpath):
    lxml_object = html.fromstring(str(soup))
    elements = lxml_object.xpath(xpath)
    return elements
