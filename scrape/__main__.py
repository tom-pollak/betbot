from .coral import scrape_coral
# from .williamhill import scrape_hill
from .smarkets import scrape_smarkets
from .soccer_api import scrape_888, scrape_uni, scrape_365


def scrape():
    bookies = {}
    smarkets_games = scrape_smarkets()
    bookies['smarkets'] = smarkets_games

    smarket_bet_games = scrape_smarkets('offer')
    bookies['smarket_bet'] = smarket_bet_games

    sport_888_games = scrape_888()
    bookies['888sport'] = sport_888_games

    uni_games = scrape_uni()
    bookies['unibet'] = uni_games

    bet_365_games = scrape_365()
    bookies['bet365'] = bet_365_games

    coral_games = scrape_coral()
    print(coral_games)
    bookies['coral'] = coral_games

    # hill_games = scrape_hill()
    # bookies['williamhill'] = hill_games

    print(bookies)
    return bookies
