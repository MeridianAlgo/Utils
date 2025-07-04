# Gemini API Chatbot

This project provides simple command-line chatbots for Google's Gemini API in both Python and Node.js.

## Features
- Chat with Gemini using the latest high-throughput model (`gemini-2.5-flash`)
- Works in both Python and Node.js
- Easy to run from the terminal

## Requirements
- Node.js v18+ (for Node.js chatbot)
- Python 3.9+ (for Python chatbot)
- A valid Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

## Setup
1. **Clone or download this repository.**
2. **Install dependencies:**
   - For Python:
     ```sh
     pip install -r requirements.txt
     ```
   - For Node.js:
     ```sh
     npm install
     ```
3. **Set your Gemini API key:**
   - The API key is currently set directly in both `chatbot.py` and `chatbot.js` for demonstration.
   - **Recommended for production:** Use a `.env` file to store your API key securely.

## Using a `.env` File (Recommended)

1. **Create a file named `.env` in your project root:**
   ```
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```
2. **Update your code:**
   - For Python, make sure you have these lines at the top:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```
     And use `os.getenv("GEMINI_API_KEY")` to access the key.
   - For Node.js, add this at the top:
     ```js
     import 'dotenv/config';
     ```
     And use `process.env.GEMINI_API_KEY` to access the key.
3. **Remove the hardcoded API key from your code for security.**

## Usage

### Python
Run the chatbot with:
```sh
python chatbot.py
```
Type your message and press Enter. Type `exit` to quit.

### Node.js
Run the chatbot with:
```sh
node chatbot.js
```
Type your message and press Enter. Type `exit` to quit.

## File Overview
- `chatbot.py`: Python CLI chatbot using the Gemini API.
- `chatbot.js`: Node.js CLI chatbot using the Gemini API.
- `requirements.txt`: Python dependencies.
- `package.json`: Node.js dependencies.
- `README.md`: This documentation file.

## Security Note
**Never share your API key publicly.** For production, always use environment variables or a `.env` file to keep your key secure.

## References
- [Gemini API Quickstart (Python)](https://ai.google.dev/gemini-api/docs/quickstart?lang=python)
- [Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits) 
