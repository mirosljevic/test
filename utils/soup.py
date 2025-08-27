from requests import Response
from bs4 import BeautifulSoup


def fetch(data):
    if isinstance(data, Response):
        return BeautifulSoup(data.text, 'html.parser')
    else:
        return BeautifulSoup(data, 'html.parser')
