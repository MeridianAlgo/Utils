<<<<<<< HEAD
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
=======
# Finnhub WebSocket Utility (USES Finnhub API)

**This utility uses the Finnhub API (WebSocket) to fetch real-time price updates.** All other logic and data are managed locally for learning and experimentation.

This project is a utility for connecting to the Finnhub WebSocket API to receive real-time stock or cryptocurrency price updates using Python. It is designed for educational and practical use.

## Features
- Connects to Finnhub WebSocket API
- Subscribes to real-time trade data for a specified symbol (stock or crypto)
- Prints formatted trade data to the console
- Easy to configure and extend
- **Beginner-friendly:** All code is commented for learning

## Requirements
- Python 3.7 or higher (tested on 3.11+)
- The `websocket-client` package:
  ```sh
  pip install websocket-client
  ```
- A Finnhub API key ([get one here](https://finnhub.io/))

## Setup
1. Clone or download this repository.
2. Install the required package:
   ```sh
   pip install websocket-client
   ```
3. Get your Finnhub API key and set it in `finnhub.py`:
   ```python
   FINNHUB_API_KEY = 'APIKEY PUT IT WITHIN THESE QUOTES'
   ```
4. Set the `SYMBOL` variable to the stock or crypto symbol you want to track (e.g., `AAPL`, `BINANCE:BTCUSDT`).

## Usage Workflow (Step-by-Step)
1. Run the script:
   ```sh
   python finnhub.py
   ```
2. The script will connect to Finnhub and print real-time price updates for your chosen symbol.

**Note:** This tool fetches data using the Finnhub API. You need an internet connection and a valid API key.

## Educational Notes
- **How does it work?** The script connects to Finnhub's WebSocket and prints incoming trade data.
- **How is the code structured?** Each function is commented to explain its purpose. The code is designed for easy modification.
- **How can you extend it?** Try subscribing to multiple symbols, or saving the data to a file!

## License
MIT

## References
- [Finnhub API Docs](https://finnhub.io/docs/api) 
>>>>>>> 8944b09 (Initial commit: Comprehensive Python & JS Finance Utilities for Beginners (API & API-free, with detailed docs))
