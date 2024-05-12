from portfolio import Portfolio


def main():
    portfolio = Portfolio()
    print("Hello welcome to the CLI stock portfolio analyzer")
    while True:

        choice1 = input("would you like a review (y/n)?")
        if choice1 == "y":
            portfolio.portfolio_review()
        elif choice1 == "n":
            pass
        else:
            raise Exception("Incorrect input")
        choice2 = input("would you like to update your portfolio (y/n)?")
        if choice2 == "y":
            subschoice = input("Would you like to add or remove a stock (a/r)")
            if subschoice == "a":
                print("To Add please enter:")
                symbol = input("Stock Symbol")
                quantity = input("Quantity")
                Purchase_price = input("Purchase Price")
                try:
                    portfolio.add_stock(symbol, quantity, Purchase_price)
                except ValueError:
                    print("Sorry stock could not be added review inputs")
            if subschoice == "r":
                print("To Remove please enter:")
                symbol = input("Stock Symbol")
                try:
                    portfolio.stocks = portfolio.remove_stock(symbol)
                except ValueError:
                    print("Sorry stock could not be removed review inputs")

        elif choice2 == "n":
            pass
        else:
            raise Exception("Incorrect input")
        Quit = input("Do you want to quit `(y/n)")
        if Quit == 'y':
            break
        elif Quit == 'n':
            pass
        else:
            raise Exception("Incorrect input")
    SystemExit


if __name__ == "__main__":
    main()
