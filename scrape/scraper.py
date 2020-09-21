import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from socket import timeout


def convert_odds(odd):
    nom, denom = odd.split('/')
    return (int(nom) / int(denom)) + 1


def get_html(
    url,
    headers={
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }):

    try:
        print('%s - Scraping...' % url)
        res = Request(url=url, headers=headers)
        html = urlopen(res, timeout=5).read()
    except HTTPError as e:
        print('%s - ERROR: Status Code %s' % (url, e.code))
        return None
    except timeout as e:
        print('%s - Socket timed out' % url)
        return None

    soup = BeautifulSoup(html, 'html.parser')
    return soup


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
