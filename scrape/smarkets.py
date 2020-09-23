from .scraper import get_html, convert_odds

URLS = [
    'https://smarkets.com/listing/sport/football/england-premier-league',
    'https://smarkets.com/listing/sport/football/england-championship',
    'https://smarkets.com/listing/sport/football/england-league-1',
    'https://smarkets.com/listing/sport/football/england-league-2',
    'https://smarkets.com/listing/sport/football/spain-la-liga',
    'https://smarkets.com/listing/sport/football/spain-la-liga-2',
    'https://smarkets.com/listing/sport/football/germany-bundesliga',
    'https://smarkets.com/listing/sport/football/france-ligue-1',
    # 'https://smarkets.com/listing/sport/football/france-ligue-2',
    'https://smarkets.com/listing/sport/football/italy-serie-a',
]


def get_odds(url, bet_or_lay='bid'):
    soup = get_html(url)
    games = []
    if soup:
        content = soup.find_all(
            'li',
            attrs={
                'class': ['item-tile', 'event-tile', 'upcoming', 'layout-row']
            })

        for div in content:
            game_odds = []
            game_names = []
            game_stakes = []
            game_name = div.find_all('div', attrs={'class': 'team'})
            for name in game_name:
                game_names.append(name.getText())

            offer = div.find_all('span', attrs={'class': bet_or_lay})
            for off in offer:
                odd = off.find_all('span', attrs={'class': 'price'})
                stake = off.find_all('span', attrs={'class': 'stake'})
                if odd:
                    game_odds.append(str(odd[0].getText()))
                    game_stakes.append(str(stake[0].getText().replace('£',
                                                                      '')))
                else:
                    game_odds.append('9999')
                    game_stakes.append('0')
            game = {
                'teams': game_names, 'odds': game_odds, 'stakes': game_stakes
            }
            games.append(game)
    return games


def scrape_smarkets(bet_or_lay='bid'):
    print('Scraping smarkets...')
    games = []
    for url in URLS:
        count = 0
        retry = True
        while retry and count < 5:
            retry = False
            league_games = get_odds(url, bet_or_lay)
            for game in league_games:
                for odd in game['odds']:
                    if odd == '\xa0':
                        retry = True
                    elif odd == '':
                        print('odds are empty')
                        odd = '9999'
            count += 1
            print('retrying', url)
        games += league_games
    return games
