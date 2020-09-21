from scrape.__main__ import scrape
from calc.output import output_odds
from calc.find_pos_bets import find_bets
import sys
import os

sites = scrape()
output_odds(sites)
find_bets(sites)
