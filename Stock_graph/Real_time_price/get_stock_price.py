# Web se data lene ke liye requests library import kar rahe hain
import requests

# HTML ko parse (read/scrape) karne ke liye BeautifulSoup import kar rahe hain
from bs4 import BeautifulSoup

# Date aur time lene ke liye datetime module
from datetime import datetime


# Function jo latest stock price laata hai
def get_latest_price(ticker):
    host = "https://www.google.com"               # Base URL (Google)
    api = f"finance/quote/{ticker}:NASDAQ"        # Stock ke liye API path (ticker ke sath)
    url = f"{host}/{api}"                         # Final URL create karna

    # Website se HTML data lena
    html = requests.get(url)

    # HTML data ko BeautifulSoup ke through parse karna
    soup = BeautifulSoup(html.text, 'html.parser')

    # Page ke andar specific div (class="YMlKec fxKbKc") se price nikalna
    text_val = soup.find('div', attrs={'class': 'YMlKec fxKbKc'}).text

    # Price return kar dena
    return text_val

# ensure karta hai code tabhi chale jab file directly run ho.
if __name__ == "__main__":       
    ticker = input("Enter stock ticker: ").upper()     # User se stock symbol lena (uppercase me)
    price = get_latest_price(ticker)                   # Function se price lana
    date = datetime.now().date()                       # Aaj ki date lena
    print(f"{ticker} price on {date}: {price}")        # Output print karna
