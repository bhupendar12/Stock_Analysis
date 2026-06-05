from Real_time_price.get_stock_price import get_latest_price  
from Stock_graph.Stock_graph import show_stock_graph  
from datetime import datetime  

def main():  # Main function define kar rahe hain jahan se program ka execution start hoga
    ticker = input("Enter stock ticker (e.g. AAPL, TSLA): ").upper()  # User se stock ticker input lena (jaise: AAPL, TSLA, MSFT)

    # Step 1: Real-time price fetch karna 
    print("\nFetching real-time price...")     # User ko batana ki price fetch ho raha hai

    # get_latest_price() function ko call karke price lena
    price = get_latest_price(ticker)

    # Aaj ki current date lena
    date = datetime.now().date()

    # Date ke sath stock price print karna
    print(f"{ticker} price on {date}: {price}")

    #  Step 2: 30-day graph show karna 
    print("\nLoading 30-day stock graph...")   # User ko batana ki graph load ho raha hai

    # show_stock_graph() function ko call karna graph dikhane ke liye
    show_stock_graph(ticker)


# Agar file directly run ho rahi hai (import nahi ki gayi)
if __name__ == "__main__":
    # Tab main() function execute karna
    main()
