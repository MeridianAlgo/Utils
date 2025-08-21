<<<<<<< HEAD
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
=======
# Alpaca News Fetcher (USES Alpaca API)

**This utility uses the Alpaca API to fetch news.** All other logic and data are managed locally for learning and experimentation.

This is a Node.js script to fetch recent news articles for a given stock or crypto symbol using the Alpaca Market Data API.

## Features
- Fetches recent news for stocks or crypto
- Interactive prompts for symbol and time window
- Uses environment variables for secure API credential management
- **Beginner-friendly:** All code is commented for learning

## Requirements
- Node.js
- An Alpaca API key and secret ([get them here](https://alpaca.markets/))

## Setup
1. Clone or download this repository.
2. Install dependencies:
   ```sh
   npm install axios
   ```
3. Set your Alpaca API credentials in `fetchNews.js` or use a `.env` file.

## Usage Workflow (Step-by-Step)
1. Run the script:
   ```sh
   node fetchNews.js
   ```
2. Follow the prompts:
   - Enter the symbol (e.g., `AAPL`, `BTCUSD`)
   - Enter the number of hours back to fetch recent news
3. The script will fetch and print the news articles.

**Note:** This tool fetches news using the Alpaca API. You need an internet connection and valid API credentials.

## Educational Notes
- **How does it work?** The script sends your request to the Alpaca API and prints the response.
- **How is the code structured?** Each function is commented to explain its purpose. The code is designed for easy modification.
- **How can you extend it?** Try adding support for filtering news by keyword, or saving results to a file!

## License
MIT

## References
- [Alpaca News API Documentation](https://docs.alpaca.markets/reference/news-3) 
>>>>>>> 8944b09 (Initial commit: Comprehensive Python & JS Finance Utilities for Beginners (API & API-free, with detailed docs))
- [Alpaca News API Documentation](https://docs.alpaca.markets/reference/news-3) 