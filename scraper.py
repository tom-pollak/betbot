from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


def convert_odds(odd):
    nom, denom = odd.split('/')
    return (int(nom) / int(denom)) + 1


def get_html(url):
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
    }

    req = Request(url=url, headers=headers)
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup
