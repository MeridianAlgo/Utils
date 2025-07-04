# Alpaca News Fetcher

This is a Node.js script to fetch recent news articles for a given stock or crypto symbol using the Alpaca Market Data API.

## Setup

1. **Install dependencies:**
   ```bash
   npm install axios
   ```
2. **Set your Alpaca API credentials:**
   Edit `fetchNews.js` and replace the placeholders for `API_KEY` and `API_SECRET` with your Alpaca API key and secret.

## Usage

Run the script:
```bash
node fetchNews.js
```

You will be prompted to enter:
- The symbol (e.g., `AAPL` for Apple, `BTCUSD` for Bitcoin/USD)
- The number of hours back to fetch recent news (press Enter for the default of 24 hours)

Example session:
```
$ node fetchNews.js
Enter the symbol (e.g., AAPL, BTCUSD): AAPL
How many hours back for recent news? (default 24): 12
Fetching news with criteria: { symbol: 'AAPL', start: '2025-07-03T06:15:20.541Z' }
...
```

## Customization
- You can change the default number of hours in the script if you want a different default window.
- The script fetches the latest news for the symbol you provide, from the Alpaca Market Data API.

## Requirements
- Node.js
- An Alpaca API key and secret ([get them here](https://alpaca.markets/))

## Reference
- [Alpaca News API Documentation](https://docs.alpaca.markets/reference/news-3) 