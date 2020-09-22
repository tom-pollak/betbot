from soccerapi.api import Api888Sport
from soccerapi.api import ApiUnibet
from soccerapi.api import ApiBet365
from soccerapi.api.base import NoOddsError

countries = {
    'england': ['premier_league', 'championship', 'league_one', 'league_two'],
    'france': ['ligue_1', 'ligue_2'],
    'germany': ['bundesliga'],
    'italy': ['serie_a'],
    'spain': ['la_liga', 'la_liga_2']
}


def scrape_888():
    print('Scraping 888 sport...')
    api = Api888Sport()
    games = scrape_api(api)
    return games


def scrape_uni():
    print('Scraping unibet...')
    api = ApiUnibet()
    games = scrape_api(api)
    return games


def scrape_365():
    print('Scraping bet365...')
    api = ApiBet365()
    games = scrape_api(api)
    print('bet365', games)
    return games


def scrape_api(api):
    games = []
    for country in countries:
        for league in countries[country]:
            try:
                odds = api.odds(country, league)
                for game in odds:
                    teams = [game['home_team'], game['away_team']]
                    odds_list = [
                        game['full_time_resut']['1'] / 1000,
                        game['full_time_resut']['X'] / 1000,
                        game['full_time_resut']['2'] / 1000
                    ]
                    game_list = {'teams': teams, 'odds': odds_list}
                    games.append(game_list)

            except TypeError:
                print(league)
            except KeyError:
                pass
            except NoOddsError:
                pass

    return games
