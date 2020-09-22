from .scraper import get_html, convert_odds

import requests
from bs4 import BeautifulSoup as bs
# import pandas as pd
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Referer': 'https://sports.williamhill.com/',
    'X-Requested-With': 'XMLHttpRequest',
}
r = requests.get(
    'https://sports.williamhill.com/betting/en-gb/football/competitions/OB_TY295/English-Premier-League/matches/OB_MGMB/Match-Betting',
    headers=headers)
print(r.content)
soup = bs(r.content, 'lxml')
print(soup)


def scrape_hill():
    url = 'https://sports.williamhill.com/betting/en-gb/football/competitions/OB_TY295/English-Premier-League/matches/OB_MGMB/Match-Betting'
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'Referer':
        'https://sports.williamhill.com/betting/en-gb/football/competitions/OB_TY295/English-Premier-League/matches/OB_MGMB/Match-Betting'
    }

    # soup = get_html(url, headers)
    results = {}
    for item in soup.select('.btmarket:has([data-odds])'):
        print(item)
        match_name = item.select_one('.btmarket__name[title]')['title']
        odds = [i['data-odds'] for i in item.select('[data-odds]')]
        row = {
            'event-starttime': item.select_one('[datetime]')['datetime'],
            'match_name': match_name,
            'home_name': match_name.split(' vs ')[0],
            'home_odds': "'" + str(odds[0]),
            'home_odds': odds[0],
            'away_name': match_name.split(' vs ')[1],
            'away_odds': odds[1],
            'away_odds': "'" + str(odds[1])
        }
        results.append(row)
    print(results)
    # print(soup)
    # content_divs = soup.find_all(
    #     'article', attrs={'class': ['sp-o-market', 'sp-o-market--default']})
    # print(content_divs)
    #
    # for div in content_divs:
    #     print(div.getText())
    #     game_name = div.find('main', attrs={'class': 'sp-o-market__title'})
    #     game_odds = div.find_all('button', attrs={'class': 'sp-betbutton'})
    #     for game in game_name:
    #         print('%s ' % (game.getText()), end='')
    #     print()
    #
    #     for i in range(3):
    #
    #         if i == 0:
    #             team = 'HOME'
    #         elif i == 1:
    #             team = 'DRAW'
    #         else:
    #             team = 'AWAY'
    #         # odd = convert_odds(game_odds[i].getText())
    #         odd = game_odds[i].getText()
    #
    #         print('%s: %s    ' % (team, odd), end='')
    #     print('\n\n')
