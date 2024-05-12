import yfinance as yf


def get_stock_value(symbol):
    """
    Fetches historical stock data from Yahoo Finance.
    :param symbol: The stock symbol to fetch data for.
    """
    stock_data = yf.Ticker(symbol)
    current_value = stock_data.info['currentPrice']
    return int(current_value)
