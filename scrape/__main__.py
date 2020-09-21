from .coral import scrape_coral
from .williamhill import scrape_hill
from .smarkets import scrape_smarkets


# scrape_hill()
def scrape():
    smarkets_games = scrape_smarkets()
    coral_games = scrape_coral()

    return {'coral': coral_games, 'smarkets': smarkets_games}
