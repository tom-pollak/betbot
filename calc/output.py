from scrape.scraper import convert_odds


def output_odds(sites):
    for site in sites:
        print('\n')
        print('------%s------' % site.upper())
        for game in sites[site]:
            print('%s v %s' % (game['teams'][0], game['teams'][1]))
            for i in range(3):
                odd = game['odds'][i]
                team = get_team(i)
                print('%s: %s    ' % (team, odd), end='')
            print('\n\n')


def get_team(i):
    if i == 0:
        team = 'HOME'
    elif i == 1:
        team = 'DRAW'
    else:
        team = 'AWAY'
    return team
