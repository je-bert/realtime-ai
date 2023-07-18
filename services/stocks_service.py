import yfinance as yf

def get_stock_data(ticker_symbol):
    """Get the stock data for the last 1 day"""

    # Fetch the live stock data
    stock_data = yf.download(ticker_symbol, period="1d", interval="1m")

    # Save the data to a text file
    data_file = f"data/{ticker_symbol}.txt"

    with open(data_file, "w") as file:
        file.write(f"Ticker Symbol: {ticker_symbol}\n\n")
        file.write(stock_data.to_csv())

    print("Stock data exported successfully to", data_file)