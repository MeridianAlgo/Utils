# Finance & AI Utilities Collection

Welcome to the **Finance & AI Utilities Collection**! This repository contains a suite of beginner-friendly, well-documented tools for finance, data analysis, and AI development. Each utility is organized in its own folder, with detailed READMEs and code comments to help you learn and build your own projects.

---

## 🚦 Visual Workflow

```mermaid
graph TD;
    A[Start Here: README.md] --> B[Pick a Utility Folder]
    B --> C1[Portfolio Tracker (yfinance API)]
    B --> C2[Options Chain Simulator (NO API)]
    B --> C3[Technical Indicators (NO API)]
    B --> C4[Order Execution Simulator (NO API)]
    B --> C5[Economic Calendar Simulator (NO API)]
    B --> C6[Dividend Tracker (NO API)]
    B --> C7[Currency Converter (NO API)]
    B --> C8[Sentiment Analysis on News (NO API)]
    B --> C9[AI Development (Gemini API)]
    B --> C10[Historical Data (Alpaca API)]
    B --> C11[News Fetching (Alpaca API)]
    B --> C12[Logging (NO API)]
    B --> C13[Websocket Connection (Finnhub API)]
    C1 --> D[Follow README instructions]
    C2 --> D
    C3 --> D
    C4 --> D
    C5 --> D
    C6 --> D
    C7 --> D
    C8 --> D
    C9 --> D
    C10 --> D
    C11 --> D
    C12 --> D
    C13 --> D
    D --> E[Run, Learn, Experiment!]
```

---

## 🗺️ Learning Roadmap

1. **Absolute Beginner**
   - Start with: `UTILS - Logging`, `UTILS - Currency Converter`
   - Learn: Python basics, file I/O, CLI menus
2. **Finance Fundamentals**
   - Try: `UTILS - Portfolio Tracker`, `UTILS - Dividend Tracker`, `UTILS - Order Execution Simulator`
   - Learn: Portfolio math, order types, dividend income
3. **Data Analysis & Technicals**
   - Try: `UTILS - Technical Indicators`, `UTILS - Sentiment Analysis on News`
   - Learn: Moving averages, RSI, MACD, basic NLP
4. **Market Simulation**
   - Try: `UTILS - Economic Calendar`, `UTILS - Options Chain Simulator`
   - Learn: Economic events, options math, scenario analysis
5. **APIs & Real Data**
   - Try: `UTILS - Portfolio Tracker` (yfinance), `UTILS - AI Development`, `UTILS - Historical Data`, `UTILS - News Fetching`, `UTILS - Websocket Connection`
   - Learn: Using APIs, real-time data, AI chatbots

---

## 📁 Utility Folders Overview

| Folder Name                        | Description                                                                                 | API Usage |
|------------------------------------|---------------------------------------------------------------------------------------------|-----------|
| **UTILS - AI Development**         | Simple chatbots for Google's Gemini API (Python/Node.js).                                   | Gemini API|
| **UTILS - Historical Data**        | Fetch historical OHLCV bars for stocks/crypto (Alpaca API, Node.js).                        | Alpaca API|
| **UTILS - Logging**                | Logging utilities for Python and Node.js. Add, read, edit, and delete log entries.           | NO API    |
| **UTILS - News Fetching**          | Fetch recent news for stocks/crypto using Alpaca API (Node.js).                             | Alpaca API|
| **UTILS - Websocket Connection**   | Real-time price updates from Finnhub WebSocket API (Python).                                | Finnhub API|
| **UTILS - Portfolio Tracker**      | Track your portfolio with automatic price fetching (Python, yfinance, beginner-friendly).   | yfinance API|
| **UTILS - Options Chain Simulator**| Simulate options chains, pricing, and Greeks (Python, no APIs, educational).                | NO API    |
| **UTILS - Technical Indicators**   | Calculate SMA, EMA, RSI, MACD for any price series (Python, no APIs, educational).          | NO API    |
| **UTILS - Order Execution Simulator** | Simulate buy/sell orders and track a virtual portfolio (Python, no APIs, educational).   | NO API    |
| **UTILS - Economic Calendar**      | Simulate economic events and their impact (Python, no APIs, educational).                   | NO API    |
| **UTILS - Dividend Tracker**       | Track upcoming dividends and expected income (Python, no APIs, educational).                | NO API    |
| **UTILS - Currency Converter**     | Convert between currencies using your own rates (Python, no APIs, educational).             | NO API    |
| **UTILS - Sentiment Analysis on News** | Analyze news sentiment with a rule-based approach (Python, no APIs, educational).      | NO API    |

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Utils-main
   ```
2. **Install dependencies:**
   - Each utility folder has its own `README.md` and lists required packages (e.g., `yfinance`, `node-fetch`, etc.).
   - For Python utilities:
     ```sh
     pip install -r requirements.txt  # if provided, or see the folder README
     ```
   - For Node.js utilities:
     ```sh
     npm install  # in the relevant folder
     ```
3. **Run utilities:**
   - Each script is run from its folder, e.g.:
     ```sh
     python portfolio_tracker.py
     node fetchNews.js
     ```

---

## 📚 Documentation

- Each folder contains a detailed `README.md` with:
  - Features
  - Setup and usage instructions
  - Example sessions
  - Learning notes and code explanations
- All code is commented for beginners and self-learners.

---

## 🧪 Testing

- The `tests/` folder contains scripts to test the main features of each utility.
- Run Python tests with:
  ```sh
  python tests/test_portfolio_tracker.py
  # or run all: python -m unittest discover -s tests
  ```
- For Node.js test scripts, run:
  ```sh
  node tests/test_logger_js.js
  ```

---

## 📝 License

This repository is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome! Please open an issue or pull request.

---

## 📖 Learning & References

- [Python Official Docs](https://docs.python.org/3/)
- [yfinance documentation](https://github.com/ranaroussi/yfinance)
- [Yahoo Finance Ticker Symbols](https://finance.yahoo.com/lookup)
- [Alpaca API Docs](https://alpaca.markets/docs/)
- [Finnhub API Docs](https://finnhub.io/docs/api)
- [Node.js](https://nodejs.org/)
- [Google Gemini API](https://ai.google.dev/gemini-api/docs/)
- [Investopedia - Financial Education](https://www.investopedia.com/)
- [Khan Academy - Finance & Capital Markets](https://www.khanacademy.org/economics-finance-domain/core-finance)
- [Real Python Tutorials](https://realpython.com/)
- [Awesome Python Finance](https://github.com/wilsonfreitas/awesome-quant)

---

Happy learning and building! 🚀
