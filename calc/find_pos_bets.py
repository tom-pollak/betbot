from .output import get_team


def find_arbitrage(bookies, match_name):
    found = False
    for bookie in bookies:
        if bookie != 'smarkets':
            for i in range(3):
                odd1 = [bookies[bookie][i], bookie, i]
                odd2, odd3 = get_other_bookies_arbitrage_odds(bookies, bookie, i)
                if 9999 not in [odd1[0], odd2[0], odd3[0]]:
                    if float(1 / odd1[0] + 1 / odd2[0] +
                             1 / odd3[0]) < float(1):
                        output_arbitrage(match_name, odd1, odd2, odd3)
                        found = True
    return found


def output_arbitrage(match_name, *odds):
    print(odds)
    odds = sorted(odds, key=lambda x: x[2])
    print('Arbitrage match found! %s' % match_name)
    for odd in odds:
        print('%s: %s - %s' % (get_team(odd[2]), odd[1], odd[0]))
    print()


def get_other_bookies_arbitrage_odds(bookies, mas_bookie, i):
    odds = ()
    for j in range(3):
        odd = 9999
        if i != j:
            for bookie in bookies:
                if bookie not in [mas_bookie, 'smarkets']:
                    if bookies[bookie][j] < odd:
                        odd = bookies[bookie][j]
            odds = odds + ([odd, bookie, j], )
            # temporary
            for odd in odds:
                if 9999 in odd:
                    print(odds)
    return odds


def find_bets(sites):
    found = False
    games = iterate_sites(sites)
    for game in games:
        bookies = games[game][0]
        match_name = games[game][1]
        found_lays = find_pos_lays(bookies, match_name)
        found_arb = find_arbitrage(bookies, match_name)
        if found_lays or found_arb:
            found = True
    if not found:
        print('No matches found')


def find_pos_lays(bookies, match_name):
    found = False
    for bookie in bookies:
        if bookie != 'smarkets' and 'smarkets' in bookies:
            for i in range(3):
                if float(bookies[bookie][i]) > float(bookies['smarkets'][i]):
                    output_match(match_name,
                                 bookies[bookie][i],
                                 bookies[bookie],
                                 bookies['smarkets'][i],
                                 'smarkets',
                                 i)
                    found = True
    return found


def iterate_sites(sites):
    games = {}
    for book_site in sites:
        for book_game in sites[book_site]:
            for alt_site in sites:
                for alt_game in sites[alt_site]:
                    if book_game['teams'][0][:3] == alt_game['teams'][
                            0][:3] and book_game['teams'][1][:3] == alt_game[
                                'teams'][1][:3]:
                        teams = book_game['teams'][0][:3] + book_game['teams'][
                            1][:3]
                        if teams not in games:
                            game = [
                                {
                                    book_site: book_game['odds'],
                                    alt_site: alt_game['odds']
                                },
                                '%s v %s' %
                                (book_game['teams'][0], book_game['teams'][1])
                            ]
                            games[teams] = game
                        else:
                            if book_site not in games[teams]:
                                games[teams][0][book_site] = book_game['odds']
                            if alt_site not in games[teams]:
                                games[teams][0][alt_site] = alt_game['odds']
    return games


def output_match(match_name, book_odds, book_site, alt_odds, alt_site, i):
    team = get_team(i)
    print('Match found! %s' % (match_name))
    print('%s odds: %s \t %s odds: %s' %
          (book_site, book_odds, alt_site, alt_odds))
    print()
