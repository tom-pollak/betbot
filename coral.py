from .scraper import get_html, convert_odds


def scrape_coral():
    url = 'https://sports.coral.co.uk/competitions/football/football-england/premier-league'
    soup = get_html(url)
    content_divs = soup.find_all('div', attrs={'class': 'odds-content'})

    for div in content_divs:
        game_name = div.find('div', attrs={'class': 'odds-names'})
        game_odds = div.find_all('span', attrs={'class': 'odds-price'})
        for game in game_name:
            print('%s ' % (game.getText()), end='')
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
