import json

import argparse

from yahoo import Yahoo

def run():
    argparser = argparse.ArgumentParser(description='Yahoo Finance Historical Data')
    argparser.add_argument("-s", "--symbol", help="stock symbol", required=True)
    args = argparser.parse_args()

    symbol = args.symbol

    yahoo = Yahoo()
    df = yahoo.request_historical_data(symbol, 'max')

    json = df.to_json(orient='index')
    print(json)

run()