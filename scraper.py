import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def extract_data(soup, selector):
    data = soup.select(selector)
    return data
