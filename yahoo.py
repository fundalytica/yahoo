import yfinance

class Yahoo:
    def request_quote(self, symbol):
        ticker = yfinance.Ticker(symbol)
        info = ticker.info
        info =  {k: v for (k, v) in info.items() if v != 'null' }
        return info

    def request_historical_data(self, symbol, range):
        ticker = yfinance.Ticker(symbol)
        history = ticker.history(period=range)
        return history