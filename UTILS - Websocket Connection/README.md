# Finnhub WebSocket Utility

This project is a utility for connecting to the Finnhub WebSocket API to receive real-time stock or cryptocurrency price updates using Python. It is designed for educational and practical use.

## Features
- Connects to Finnhub WebSocket API
- Subscribes to real-time trade data for a specified symbol (stock or crypto)
- Prints formatted trade data to the console
- Easy to configure and extend

## Requirements
- Python 3.7 or higher (tested on 3.11+)
- The `websocket-client` package (may already be installed on some systems)

To ensure you have the required package, you can run:
```
pip install websocket-client
```

## Setup

1. **Get a Finnhub API Key:**
   - Sign up at [Finnhub.io](https://finnhub.io/) and get your free API key.
2. **Set your API key:**
   - Open `finnhub.py` and set your API key directly in the file:
     ```python
     FINNHUB_API_KEY = 'APIKEY PUT IT WITHIN THESE QUOTES' 
     ```
3. **Choose your symbol:**
   - Set the `SYMBOL` variable to the stock or crypto symbol you want to track (e.g., `AAPL` for Apple, `BINANCE:BTCUSDT` for Bitcoin/USDT).

## Usage

Run the script with:
```
python finnhub.py
```

## Notes
- Free Finnhub accounts may have limited access to certain symbols or WebSocket features.
- If you see a 401 error, double-check your API key and account status.
- The script is set to run for a limited time (e.g., 30 seconds) and then close automatically.
- The `websocket-client` package is recommended for compatibility, but some Python distributions may already include WebSocket support.

## About
This project is a simple utility for developers, students, and hobbyists who want to quickly connect to Finnhub's WebSocket API and see real-time price data in action. It is intended for educational and utility purposes. 