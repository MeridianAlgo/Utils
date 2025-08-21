<<<<<<< HEAD
const axios = require('axios');
const readline = require('readline');

// Replace with your Alpaca API Key and Secret
const API_KEY = 'ALPACA_API_KEY';
const API_SECRET = 'ALPACA_API_SECRET';

// Set up readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt user for symbol and hours
rl.question('Enter the symbol (e.g., AAPL, BTCUSD): ', (symbol) => {
  rl.question('How many hours back for recent news? (default 24): ', (hoursInput) => {
    const hours = parseInt(hoursInput) || 24;
    // Calculate the start time for recent news
    const now = new Date();
    const since = new Date(now.getTime() - hours * 60 * 60 * 1000);
    const startISO = since.toISOString();

    const fetchNews = async () => {
      try {
        const params = {};
        if (symbol) params.symbols = symbol;
        params.start = startISO; // Only fetch news from the last N hours

        const response = await axios.get('https://data.alpaca.markets/v1beta1/news', {
          headers: {
            'APCA-API-KEY-ID': API_KEY,
            'APCA-API-SECRET-KEY': API_SECRET,
          },
          params
        });

        const news = response.data.news;
        if (!news || news.length === 0) {
          console.log('No news found for the given criteria.');
          rl.close();
          return;
        }
        news.forEach((article, idx) => {
          console.log(`\n[${idx + 1}] ${article.headline}`);
          console.log(`Source: ${article.source}`);
          console.log(`Summary: ${article.summary}`);
          console.log(`URL: ${article.url}`);
          console.log('---');
        });
      } catch (error) {
        console.error('Error fetching news:', error.response ? error.response.data : error.message);
      } finally {
        rl.close();
      }
    };

    console.log('Fetching news with criteria:', { symbol, start: startISO });
    fetchNews();
  });
=======
const axios = require('axios');
const readline = require('readline');

// Replace with your Alpaca API Key and Secret
const API_KEY = 'ALPACA_API_KEY';
const API_SECRET = 'ALPACA_API_SECRET';

// Set up readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Prompt user for symbol and hours
rl.question('Enter the symbol (e.g., AAPL, BTCUSD): ', (symbol) => {
  rl.question('How many hours back for recent news? (default 24): ', (hoursInput) => {
    const hours = parseInt(hoursInput) || 24;
    // Calculate the start time for recent news
    const now = new Date();
    const since = new Date(now.getTime() - hours * 60 * 60 * 1000);
    const startISO = since.toISOString();

    const fetchNews = async () => {
      try {
        const params = {};
        if (symbol) params.symbols = symbol;
        params.start = startISO; // Only fetch news from the last N hours

        const response = await axios.get('https://data.alpaca.markets/v1beta1/news', {
          headers: {
            'APCA-API-KEY-ID': API_KEY,
            'APCA-API-SECRET-KEY': API_SECRET,
          },
          params
        });

        const news = response.data.news;
        if (!news || news.length === 0) {
          console.log('No news found for the given criteria.');
          rl.close();
          return;
        }
        news.forEach((article, idx) => {
          console.log(`\n[${idx + 1}] ${article.headline}`);
          console.log(`Source: ${article.source}`);
          console.log(`Summary: ${article.summary}`);
          console.log(`URL: ${article.url}`);
          console.log('---');
        });
      } catch (error) {
        console.error('Error fetching news:', error.response ? error.response.data : error.message);
      } finally {
        rl.close();
      }
    };

    console.log('Fetching news with criteria:', { symbol, start: startISO });
    fetchNews();
  });
>>>>>>> 8944b09 (Initial commit: Comprehensive Python & JS Finance Utilities for Beginners (API & API-free, with detailed docs))
}); 