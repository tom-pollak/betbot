from .output import get_team


def find_bets(sites):
    found = False
    for smarkets_game in sites['smarkets']:
        home_team = smarkets_game['teams'][0]
        away_team = smarkets_game['teams'][1]
        for book_site in sites:
            if book_site != 'smarkets':
                for book_game in sites[book_site]:
                    if book_game['teams'][0][:3] == home_team[:3] and book_game[
                            'teams'][1][:3] == away_team[:3]:
                        for i in range(3):
                            try:
                                if float(smarkets_game['odds'][i]) < float(
                                        book_game['odds'][i]):
                                    output_match(smarkets_game,
                                                 book_game,
                                                 i,
                                                 book_site)
                                    found = True
                            except ValueError:
                                pass
                                # print('ERROR: %s %s' %
                                #       (smarkets_game['odds'][i],
                                #        book_game['odds'][i]))
    if not found:
        print('No matches found.')


def output_match(smarkets_game, book_game, i, book_site):
    team = get_team(i)
    print('Match found! %s v %s - %s' %
          (smarkets_game['teams'][0], smarkets_game['teams'][1], team))
    print(book_game['teams'])
    print('%s odds: %s \t smarkets odds: %s' %
          (book_site, book_game['odds'][i], smarkets_game['odds'][i]))
    print()
