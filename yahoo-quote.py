import json
import datetime, pytz

import argparse

from utils import utils
from yahoo import Yahoo

def run():
    argparser = argparse.ArgumentParser(description='Yahoo Finance Quote')
    argparser.add_argument("-s", "--symbol", help="stock symbol", required=True)
    args = argparser.parse_args()

    symbol = args.symbol

    yahoo = Yahoo()
    info = yahoo.request_quote(symbol)

    bid = info['bid']
    ask = info['ask']
    previousClose = info['previousClose']

    isUSMarketOpen = (bid != 0 and ask != 0)
    nyc_datetime = datetime.datetime.now(pytz.timezone('US/Eastern'))
    date_fmt = "%B %d, %Y"
    time_fmt = "%I:%M:%S %p"

    data = {}
    data["date"] = nyc_datetime.strftime(date_fmt)
    data["time"] = nyc_datetime.strftime(time_fmt)
    data["symbol"] = args.symbol
    data["price"] = ask if isUSMarketOpen else previousClose
    data["change"] = round((ask / previousClose) - 1, 5)
    data["market"] = "open" if isUSMarketOpen else "closed"
    print(data)

run()