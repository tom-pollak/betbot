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
                if odd == 9999:
                    odd = ''
                if 'stakes' in game:
                    stake = game['stakes'][i]
                    print('%s: %s - %s    ' % (team, odd, stake), end='')
                else:
                    print('%s: %s    ' % (team, odd), end='')
            print('\n\n')
    print()


def get_team(i):
    if i == 0:
        team = 'HOME'
    elif i == 1:
        team = 'DRAW'
    else:
        team = 'AWAY'
    return team
