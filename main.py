import ccxt
import time


exchange = ccxt.binance()
symbol = "XRP/USDT"


def get_price(exchange, symbol):
    ticker = exchange.fetch_ticker(symbol)
    print(ticker)
    return ticker["last"]


def main():
    max_price = 0
    while True:
        current_price = get_price(exchange, symbol)
        if current_price > max_price:
            max_price = current_price
        if (max_price - current_price) / max_price >= 0.01:
            print("Price has dropped 1% from the maximum price in the last hour.")
        time.sleep(1)


if __name__ == "__main__":
    main()
