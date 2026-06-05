# Plot stock price graph using Yahoo Finance
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def show_stock_graph(ticker):
    # Fetch 30 days of data
    data = yf.download(ticker, period="1mo", interval="1d")

    if data.empty:
        print("Invalid ticker or no data found.")
        return

    latest_price = data['Close'].iloc[-1].item()
    date = datetime.now().date()
    print(f"{ticker} price on {date}: ${latest_price:.2f}")

    # Plot graph
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], color='green', marker='o', label='Closing Price')
    plt.title(f"{ticker} - Last 30 Days Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g. AAPL, TSLA): ").upper()
    show_stock_graph(ticker)  