from .scraper import get_html, convert_odds

URLS = [
    'https://sports.coral.co.uk/competitions/football/football-england/premier-league',
    'https://sports.coral.co.uk/competitions/football/football-england/championship',
    'https://sports.coral.co.uk/competitions/football/football-england/league-one',
    'https://sports.coral.co.uk/competitions/football/football-spain/spanish-la-liga',
    'https://sports.coral.co.uk/competitions/football/football-germany/german-bundesliga',
]


def scrape_coral():
    games = []
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
    }
    for url in URLS:
        soup = get_html(url, headers=headers)
        if soup:
            content_divs = soup.find_all('div',
                                         attrs={'class': 'odds-content'})
            for div in content_divs:
                game_name = div.find_all(
                    'span', attrs={'class': 'odds-names-opponent-name'})

                game_odds = div.find_all('span', attrs={'class': 'odds-price'})

                teams = []
                odds = []
                for name in game_name:
                    teams.append(name.getText())
                    # print('%s v %s' % (teams[0], teams[1]))

                for i in range(3):
                    print('frac odd %s' % game_odds[i].getText)
                    odd = convert_odds(game_odds[i].getText())
                    odds.append(odd)

                league_games = {'teams': teams, 'odds': odds}
                games.append(league_games)
    return games
