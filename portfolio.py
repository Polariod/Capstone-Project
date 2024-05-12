from stock_data import *


class Portfolio:
    def __init__(self):
        self.stocks = [
            {"symbol": "AAPL", "quantity": 3, "purchase price": 180}, {"symbol": "GOOG", "quantity": 5, "purchase price": 160}]

    def add_stock(self, symbol, quantity, purchase_price,):
        # Add a stock to the portfolio
        self.stocks.append(
            {"symbol": symbol, "quantity": int(quantity), "purchase price": int(purchase_price)})

    def remove_stock(self, symbol):
        # Remove a stock from the portfolio
        self.stocks[:] = [s for s in self.stocks if s.get('symbol') != symbol]
        return self.stocks

    def calculate_portfolio_value(self):
        # Calculate total portfolio value
        total_value = sum(get_stock_value(
            stock['symbol'])*stock['quantity'] for stock in self.stocks)
        return total_value

    def initial_value(self):
        init_val = sum(stock['purchase price']*stock["quantity"]
                       for stock in self.stocks)
        return init_val

    def portfolio_review(self):
        print("Portfolio Review")
        Port_val = self.calculate_portfolio_value()
        Initial_val = self.initial_value()
        for stock in self.stocks:
            Stock_val = get_stock_value(stock['symbol'])
            print(f"Holding {stock['quantity']} shares of {
                  stock['symbol']}, Total value: {Stock_val}")
        print(f"Total value {Port_val}")
        p_l = Port_val - Initial_val
        print(f"Profit/Loss {p_l}")
