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
   - For production, move the key to a `.env` file or environment variable for security.

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