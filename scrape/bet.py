import requests
import json

API_KEY = '7c4676b70197ffde079015103c971c85'


def get_games():
    res = requests.get(
        'https://api.the-odds-api.com/v3/odds/?sport=upcoming&region=uk&mkt=h2h&dateFormat=iso&apiKey=%s'
        % (API_KEY))
    if res.status_code == 200:
        return res.json()['data']


def get_postive_bets(data):
    bets = []
    for game in data:
        back_odds = [{'site': '', 'odds': 9999}, {'site': '', 'odds': 9999}]
        lay_odds = [{'site': '', 'odds': 9999}, {'site': '', 'odds': 9999}]
        for site in game['sites']:
            if 'h2h_lay' in site['odds']:
                for i in range(2):
                    if int(site['odds']['h2h_lay'][i]) < lay_odds[i]['odds']:
                        lay_odds[i]['odds'] = int(site['odds']['h2h_lay'][i])
                        lay_odds[i]['site'] = site['site_nice']

            for i in range(2):
                if int(site['odds']['h2h'][i]) < back_odds[i]['odds']:
                    back_odds[i]['odds'] = int(site['odds']['h2h'][i])
                    back_odds[i]['site'] = site['site_nice']

        for i in range(2):
            if back_odds[i]['odds'] >= lay_odds[i]['odds']:
                if i == 0:
                    team = 'home'
                if i == 1:
                    team = 'away'

                bets.append({
                    'sport': game['sport_nice'],
                    'teams': game['teams'],
                    'back': back_odds[i],
                    'lay': lay_odds[i],
                    'team': team
                })
    return bets


def output_positive_bets(bets):
    if len(bets) > 0:
        print('Positive bets found:')
    for bet in bets:
        print('BET FOUND! %s: %s v %s - %s' %
              (bet['sport'], bet['teams'][0], bet['teams'][1], bet['team']))
        print('Back: %s at odds %s' %
              (bet['back']['site'], bet['back']['odds']))
        print('Lay: %s at odds %s' % (bet['lay']['site'], bet['lay']['odds']))
        print()


def main():
    data = get_games()
    bets = get_postive_bets(data)
    output_positive_bets(bets)


main()
