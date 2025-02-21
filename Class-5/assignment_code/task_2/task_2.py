import yfinance as yf
import sqlite3
import pandas as pd
import time


db_name = "stocks.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS stock_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER)''')
conn.commit()

def fetch_stock_data(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d", interval="1m") 
        
        if data.empty:
            print(f"No data found for {symbol}. Skipping...")
            return None  

        latest = data.iloc[-1]
        print(f"Fetched Data:\n {latest}") 

        return {
            "symbol": symbol,
            "open": latest["Open"],
            "high": latest["High"],
            "low": latest["Low"],
            "close": latest["Close"],
            "volume": latest["Volume"]
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None


def store_data(symbol):
    stock_data = fetch_stock_data(symbol)
    if stock_data:
        cursor.execute('''INSERT INTO stock_data (symbol, open, high, low, close, volume)  
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (stock_data["symbol"], stock_data["open"],
                        stock_data["high"], stock_data["low"], 
                        stock_data["close"], stock_data["volume"]))
        conn.commit()
        print(f"Stored data for {symbol}")

def analyze_stock(symbol):
    df = pd.read_sql_query("SELECT * FROM stock_data WHERE symbol=? ORDER BY timestamp DESC LIMIT 100", conn, params=(symbol,))
    print(df)

symbol = "NVDA"  # Nvidia stock
for _ in range(5):  
    store_data(symbol)
    time.sleep(60)  

analyze_stock(symbol)

conn.close()
