<<<<<<< HEAD
# Gemini API Chatbot in Python
# This script allows you to chat with Google's Gemini model from the command line.
# The API key is set directly in the script for demonstration purposes.
# For production, consider using a .env file or environment variable for security.

from google import genai  # Official Gemini API Python SDK
import os

# Set the Gemini API key directly (replace with your own key)
os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"

# Initialize the Gemini API client (reads API key from environment variable)
client = genai.Client()

print("Gemini Chatbot (type 'exit' to quit)")

# Main chat loop
while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() == "exit":  # Exit condition
        break
    # Send the user input to Gemini and get the response
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Use the high-throughput Gemini model
        contents=user_input
    )
=======
# Gemini API Chatbot in Python
# This script allows you to chat with Google's Gemini model from the command line.
# The API key is set directly in the script for demonstration purposes.
# For production, consider using a .env file or environment variable for security.

from google import genai  # Official Gemini API Python SDK
import os

# Set the Gemini API key directly (replace with your own key)
os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"

# Initialize the Gemini API client (reads API key from environment variable)
client = genai.Client()

print("Gemini Chatbot (type 'exit' to quit)")

# Main chat loop
while True:
    user_input = input("You: ")  # Get user input
    if user_input.lower() == "exit":  # Exit condition
        break
    # Send the user input to Gemini and get the response
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # Use the high-throughput Gemini model
        contents=user_input
    )
>>>>>>> 8944b09 (Initial commit: Comprehensive Python & JS Finance Utilities for Beginners (API & API-free, with detailed docs))
    print("Gemini:", response.text)  # Print Gemini's response 