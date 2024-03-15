import yfinance as yf

#to fetch stock data from Yahoo Finance
def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return data.iloc[-1].to_dict()
        else:
            return None
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

#to add a stock to the portfolio
def add_stock(portfolio, symbol):
    stock_data = fetch_stock_data(symbol)
    if stock_data:
        portfolio[symbol] = stock_data
        print(symbol, "added to the portfolio.")
    else:
        print("Failed to fetch data for", symbol,". Please check the symbol and try again.")

# Function to remove a stock from the portfolio
def remove_stock(portfolio, symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(symbol,"removed from the portfolio.")
    else:
        print(symbol,"not found in the portfolio.")

#to display the portfolio
def display_portfolio(portfolio):
    print("\nPortfolio:")
    for symbol, data in portfolio.items():
        print(f"{symbol}: {data['Close']}")

# Main function
def main():
    portfolio = {}
    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter the stock symbol: ").upper()
            add_stock(portfolio, symbol)
        elif choice == "2":
            symbol = input("Enter the stock symbol to remove: ").upper()
            remove_stock(portfolio, symbol)
        elif choice == "3":
            display_portfolio(portfolio)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
