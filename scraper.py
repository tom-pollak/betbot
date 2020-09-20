from bs4 import BeautifulSoup
import re
from urllib.request import urlopen, Request


def convert_odds(odd):
    nom, denom = odd.split('/')
    return (int(nom) / int(denom)) + 1


def scrap_coral(soup):
    content_divs = soup.find_all('div', attrs={'class': 'odds-content'})

    for div in content_divs:
        game_name = div.find_all('div', attrs={'class': 'odds-names'})
        game_odds = div.find_all('span', attrs={'class': 'odds-price'})
        for game in game_name:
            print('%s' % (game.getText()), end='')
        print()

        for i in range(3):

            if i == 0:
                team = 'HOME'
            elif i == 1:
                team = 'DRAW'
            else:
                team = 'AWAY'
            odd = convert_odds(game_odds[i].getText())

            print('%s: %s    ' % (team, odd), end='')
        print('\n\n')


url = 'https://sports.coral.co.uk/competitions/football/football-england/premier-league'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
}

req = Request(url=url, headers=headers)
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
scrap_coral(soup)
