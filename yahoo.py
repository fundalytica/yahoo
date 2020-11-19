import json

from utils import utils

import yfinance as yf

class Yahoo:
    # def __init__(self):

    def request_quote(self, symbol):
        print(f'> request quote {symbol}')
        ticker = yf.Ticker(symbol)
        info = ticker.info
        # info =  {k: v for (k, v) in info.items() if v }
        return info

    def request_historical_data(self, symbol, range):
        print(f'> request_historical_data: {symbol}')
        ticker = yf.Ticker(symbol)
        history = ticker.history(period=range)
        return history

    def request_historical_date(self, symbol, date):
        print('historical-date')

def run():
    yahoo = Yahoo()
    symbol = 'SPY'

    # quote = yahoo.request_quote(symbol)
    # print(utils.pprint(quote))

    historical = yahoo.request_historical_data(symbol, 'max')
    print(historical)

import sys
if sys.stdin.isatty():
    print('> terminal')
    run()