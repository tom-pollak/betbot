from .scraper import get_html, convert_odds

URLS = [
    'https://smarkets.com/listing/sport/football/england-premier-league',
    'https://smarkets.com/listing/sport/football/england-championship',
    'https://smarkets.com/listing/sport/football/england-league-1',
    'https://smarkets.com/listing/sport/football/england-league-2',
    'https://smarkets.com/listing/sport/football/spain-la-liga',
    'https://smarkets.com/listing/sport/football/spain-la-liga-2',
    'https://smarkets.com/listing/sport/football/germany-bundesliga'
    'https://smarkets.com/listing/sport/football/france-ligue-1',
    'https://smarkets.com/listing/sport/football/france-ligue-2',
    'https://smarkets.com/listing/sport/football/italy-serie-a',
]


def get_odds(url):
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

            offer = div.find_all('span', attrs={'class': 'bid'})
            for off in offer:
                odd = off.find_all('span', attrs={'class': 'price'})
                stake = off.find_all('span', attrs={'class': 'stake'})
                if odd:
                    game_odds.append(str(odd[0].getText()))
                    game_stakes.append(str(stake[0].getText().replace('£',
                                                                      '')))
                else:
                    return False
            game = {
                'teams': game_names, 'odds': game_odds, 'stakes': game_stakes
            }
            games.append(game)

    return games


def scrape_smarkets():
    print('Scraping smarkets...')
    games = []
    for url in URLS:

        retry = True
        count = 0
        while retry and count < 5:
            league_games = get_odds(url)
            retry = False
            if not league_games:
                pass
                print('%s - Games not found, skipping...' % url)
            else:
                if '\xa0' in league_games[0]['odds']:
                    count += 1
                    retry = True
                    # print('%s - Odds not found, retrying...' % url)
        if league_games and count < 5:
            games += league_games
        elif not league_games:
            pass
        else:
            pass
            print('%s - Tried 5 times, skipping...' % url)
    return games
